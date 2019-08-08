from retrying import retry
import requests


class RetryBase(object):
    @classmethod
    def retry_if_io_error(cls, exception):
        """Return True if we should retry (in this case when it's an IOError), False otherwise"""
        return isinstance(exception, IOError)


class RetryOnError:
    @classmethod
    @retry(stop_max_attempt_number=10, wait_exponential_multiplier=2000, wait_exponential_max=60000, retry_on_exception=RetryBase.retry_if_io_error)
    def do_something_unreliable(cls, text):
        print("trying")
        print(text)
        resp = requests.get("http://127.0.0.1:5000/status")
        return resp

        print('Error enable_plugin: code={} resp={}'.format(resp, resp.text))
        return None


if __name__ == '__main__':
    for x in range(5):
        RetryOnError.do_something_unreliable("hi")
