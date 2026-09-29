import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from agents.final_agent import test_final_agent


if __name__ == "__main__":
    test_final_agent()