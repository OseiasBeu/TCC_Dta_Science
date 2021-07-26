import os
import dotenv
def print_env(body):
    dotenv.load_dotenv()
    # print(body)
    dict = {}
    for field in body:
        dict[field] = os.getenv(field)
    # print('=====================================================')
    # print(dict)
    
    return dict

if __name__ == "__main__":
    body = ['client_id','client_secret','dbname','host','port','user','password']
    print_env(body)
    