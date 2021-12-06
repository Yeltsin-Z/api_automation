import unittest
import api_client
import commons as cmn


class TestWhatIfDataValidation(unittest.TestCase):
    payload_data = "./What-If_Data_Validation/payload_data.json"
    headers = {"Content-Type": "application/json", "apikey": "jPrpkogvVHeS2g2t8BgicjE5KVvzqYe3"}

    def test_scenario_1(self):
        # Validating the Input Metrics / Plan Assumption Metrics
        api_endpoint = "what-ifs/62"
        q_params = {'f': ''}
        request_data = cmn.get_input_data(self.payload_data, self._testMethodName)
        api = api_client.ApiClient()
        response = api.call(request_type="get", headers=self.headers,
                            endpoint=api_endpoint, request_data=request_data, q_params=q_params)
        print(response.status_code)
        assert response.status_code == 200
        print(response.json())
        assert "Metric_1" in response.json()['whatIf']['attributes']['inputMetrics'][0]
        assert "Metric_2" in response.json()['whatIf']['attributes']['inputMetrics'][1]

    def test_scenario_2(self):
        # Validating the Target Metrics
        api_endpoint = "what-ifs/63"
        q_params = {'f': ''}
        request_data = cmn.get_input_data(self.payload_data, self._testMethodName)
        api = api_client.ApiClient()
        response = api.call(request_type="get", headers=self.headers,
                            endpoint=api_endpoint, request_data=request_data, q_params=q_params)
        print(response.status_code)
        assert response.status_code == 200
        print(response.json())
        assert "Add_Metric" in response.json()['whatIf']['attributes']['targetMetrics'][0]
        assert "Subtraction_Metric" in response.json()['whatIf']['attributes']['targetMetrics'][1]
        assert "Mul_Metrics" in response.json()['whatIf']['attributes']['targetMetrics'][2]
        assert "Div_Metrics" in response.json()['whatIf']['attributes']['targetMetrics'][3]

    def test_scenario_3(self):
        # Update Metric_1 value by 50 and Validate the Response
        api_endpoint = "what-ifs/63/update-metrics"
        request_data = cmn.get_input_data(self.payload_data, self._testMethodName)
        api = api_client.ApiClient()
        response = api.call(request_type="post", headers=self.headers,
                            endpoint=api_endpoint, request_data=request_data)
        print(response.status_code)
        assert response.status_code == 200
        print(response.json())
        api_endpoint = "what-ifs/63"
        q_params = {'f': ''}
        request_data = cmn.get_input_data(self.payload_data, self._testMethodName)
        api = api_client.ApiClient()
        response = api.call(request_type="get", headers=self.headers,
                            endpoint=api_endpoint, request_data=request_data, q_params=q_params)
        print(response.status_code)
        assert response.status_code == 200
        print(response.json())
        assert response.json()['whatIf']['metrics'][2]['displayName'] == "Metric 1"
        assert response.json()['whatIf']['metrics'][2]['data']['2022-11-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-08-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2021-12-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-10-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-02-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-03-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-01-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-05-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-04-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-09-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-07-01']['whatIf'] == 150.0
        assert response.json()['whatIf']['metrics'][2]['data']['2022-06-01']['whatIf'] == 150.0

