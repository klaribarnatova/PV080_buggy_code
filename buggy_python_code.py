import yaml
import flask
import docstring

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    if version == "2":
        return fetch_website("2", url)
    return fetch_website("3", url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class person:
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL

    try:
        http = urllib.PoolManager()
        request = http.request('GET', url)
        print(request)
    except:
        print('Exception')


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if (password != "Iloveyou"):
        print("Invalid password!")
    else:
        print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version_input = input("Choose version of urllib: [2/3]")
        if urlib_version_input == "2":
            fetch_website("2", url="https://www.google.com")
        else:
            fetch_website("3", url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
