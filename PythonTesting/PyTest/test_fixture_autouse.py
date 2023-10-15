import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code (runs before every test)
    print("\nSetting up...")
    yield
    # Teardown code (runs after every test)
    print("Tearing down...")

def test_example_1():
    print("Test 1 is running.")

def test_example_2():
    print("Test 2 is running.")
