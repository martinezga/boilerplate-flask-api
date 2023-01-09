class TestHealth:
    def test_health_response(self, client_test):
        response = client_test.get("/health/")

        json_data = response.json
        response_detail = json_data.get("detail")

        assert response.status_code == 200
        assert response_detail == "Up and running!"
