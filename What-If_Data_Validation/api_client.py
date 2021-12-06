import requests


class ApiClient():
    base_url = "https://testautomation-staging.drivetrain.ai/drive/api/v1"

    def call(self, request_type, headers, endpoint, request_data=None, q_params=None):
        if request_type == "post":
            response = requests.post(url=self.base_url + "/" + endpoint,
                                     headers=headers, json=request_data, params=q_params)
        elif request_type == "get":
            response = requests.get(url=self.base_url + "/" + endpoint,
                                    headers=headers, params=q_params)
        elif request_type == "delete":
            response = requests.delete(url=self.base_url + "/" + endpoint,
                                       headers=headers, params=q_params)
        elif request_type == "patch":
            response = requests.patch(url=self.base_url + "/" + endpoint,
                                      headers=headers, json=request_data, params=q_params)
        elif request_type == "put":
            response = requests.put(url=self.base_url + "/" + endpoint,
                                    headers=headers, json=request_data, params=q_params)
        else:
            response = None
        return response
