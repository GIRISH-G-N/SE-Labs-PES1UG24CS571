
"""Manage a simple in-memory radio show schedule."""

import ast
import operator
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE slots (id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
    "start_hour INTEGER, minutes INTEGER)"
)


def add_slot(show, host, start_hour, minutes):
    """Add a radio show to the schedule."""
    conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) "
        "VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a readable label for a radio show."""
    return f"{show} hosted by {host}"


def overlap_free(formula):
    """Safely evaluate basic arithmetic and comparison expressions."""
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Gt: operator.gt,
        ast.GtE: operator.ge,
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
    }

    def evaluate(node):
        """Evaluate only approved expression nodes."""
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float, bool):
                return node.value

        if isinstance(node, ast.BinOp):
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](
                    evaluate(node.left),
                    evaluate(node.right),
                )

        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            operation = type(node.ops[0])
            if operation in allowed_operators:
                return allowed_operators[operation](
                    evaluate(node.left),
                    evaluate(node.comparators[0]),
                )

        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, (ast.UAdd, ast.USub)):
                value = evaluate(node.operand)
                if isinstance(node.op, ast.UAdd):
                    return value
                return -value

        raise ValueError("Unsupported formula")

    try:
        expression = ast.parse(formula, mode="eval")
        return evaluate(expression)
    except (
        ValueError,
        TypeError,
        SyntaxError,
        ZeroDivisionError,
        OverflowError,
        RecursionError,
    ):
        return False


def morning_shows():
    """Return scheduled shows starting before noon."""
    return [
        row[0]
        for row in conn.execute(
            "SELECT show FROM slots WHERE start_hour < ?",
            (12,),
        )
    ]


def remove_slot(slot_id):
    """Remove a scheduled show by its ID."""
    conn.execute(
        "DELETE FROM slots WHERE id = ?",
        (slot_id,),
    )


def main():
    """Demonstrate the radio scheduling operations."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free("7 + 1 <= 13"), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
