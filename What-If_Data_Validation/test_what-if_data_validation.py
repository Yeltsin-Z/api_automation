import json
import unittest
import commons as cmn, api_client


class TestFormulaOrdering(unittest.TestCase):
    headers = {"Content-Type": "application/json", "apikey": "jPrpkogvVHeS2g2t8BgicjE5KVvzqYe3"}
    create_model_payload_file = "./formula-ordering/payloads/create-model.json"
    create_metric_payload_file = "./formula-ordering/payloads/create-metric.json"
    add_formula_payload_file = "./formula-ordering/payloads/add-formula.json"

    def test_formula_ordering(self):
        print("This is the test for formula Ordering Validation in DTML")
        print("Creating a model .... ")
        api_endpoint = "model/modules"
        request_data = cmn.get_input_data(self.create_model_payload_file)
        api = api_client.ApiClient()
        response, api_url = api.call(request_type="post", headers=self.headers,
                                     endpoint=api_endpoint, request_data=request_data)
        assert response.status_code == 200
        print("\n", api_url)
        print("\n Model created successfully..!!!")

        print("\n Creating a metric .... ")
        api_endpoint = "model/modules/Formula_Ordering/metrics"
        request_data = cmn.get_input_data(self.create_metric_payload_file)
        api = api_client.ApiClient()
        response, api_url = api.call(request_type="post", headers=self.headers,
                                     endpoint=api_endpoint, request_data=request_data)
        assert response.status_code == 200
        print("\n", api_url)
        print("\n Metric created successfully..!!!")

        print("\n Creating formulas across Dimensions .... ")
        api_endpoint = "model/modules/Formula_Ordering/metrics/metrics.formula_order_test?overwrite=true&rollup=MONTHLY,QUARTERLY,HALF_YEARLY,ANNUALLY"
        request_data = cmn.get_input_data(self.add_formula_payload_file)
        api = api_client.ApiClient()
        response, api_url = api.call(request_type="post", headers=self.headers,
                                     endpoint=api_endpoint, request_data=request_data)
        assert response.status_code == 200
        print("\n", api_url)
        print("\nSuccessfully created formula for US ")

        print("\nFetching DTML....")
        api_endpoint = "dtmls/1"
        api = api_client.ApiClient()
        response, api_url = api.call(request_type="get", headers=self.headers,
                                     endpoint=api_endpoint)
        assert response.status_code == 200
        print("\n", api_url)
        print("\nParsing DTML data....")
        dtml_data = response.json()['dtml']
        parsed_dtml = json.loads(dtml_data)
        for i in range(len(parsed_dtml['metrics'])):
            if "formula_order_test" in parsed_dtml['metrics'][i]['name']:
                self.assertEqual("metrics.formula_order_test[Country=US] = 20",
                                 parsed_dtml['metrics'][i]['formulae'][0])
                print("\nCheck 1 passed !")
                self.assertEqual("metrics.formula_order_test[Country=Japan] = 50",
                                 parsed_dtml['metrics'][i]['formulae'][1])
                print("\nCheck 2 passed !")
                self.assertEqual("metrics.formula_order_test[Country=ME] = 70",
                                 parsed_dtml['metrics'][i]['formulae'][2])
                print("\nCheck 3 passed !")
                self.assertEqual("metrics.formula_order_test[Country=APAC] = 200",
                                 parsed_dtml['metrics'][i]['formulae'][3])
                print("\nCheck 4 passed !")
                self.assertEqual("metrics.formula_order_test[Country=Canada] = 100",
                                 parsed_dtml['metrics'][i]['formulae'][4])
                print("\nCheck 5 passed !")

        print("\nDeleting the model after test ...")
        api_endpoint = "model/modules/Formula_Ordering"
        api = api_client.ApiClient()
        response, api_url = api.call(request_type="delete", headers=self.headers,
                                     endpoint=api_endpoint, request_data=request_data)
        assert response.status_code == 200
        print("\n", api_url)
        print("\n Model deleted successfully...!!!")
