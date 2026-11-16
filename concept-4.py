import pytest


@pytest.fixture
def sample_data():
    print("\n Setup: Creating test data")
    data = {"name": "Alice", "Age": 36}
    yield data
    print("cleaning up test data")

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["Age"] == 36
    print("Test executed successfully")