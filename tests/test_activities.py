def test_get_activities_returns_seeded_activities(client):
    # Arrange
    expected_activities = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Swimming Club",
        "Drama Society",
        "Art Studio",
        "Debate Team",
        "Math Olympiad",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activities.issubset(payload.keys())


def test_get_activities_includes_participant_lists(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert payload[activity_name]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]