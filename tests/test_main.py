from raid_tracker.main import greet


def test_greet_default_role():
    assert greet("Ada") == "Hello, Ada (PM)! RAID tracker coming soon."


def test_greet_custom_role():
    assert (
        greet("Ada", "PMO Lead") == "Hello, Ada (PMO Lead)! RAID tracker coming soon."
    )
