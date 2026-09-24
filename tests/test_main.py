from raid_tracker.main import greet


def test_greet():
    assert greet("Ada") == "Hello, Ada! RAID tracker coming soon."
