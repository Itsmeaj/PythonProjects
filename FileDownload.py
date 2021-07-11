import requests
import os


def download_file_from_google_drive(url, filename):
    """
    :param url: Link of the file
    :param filename:filename and format of file
    response 200:
    http response when connection is successful
    """
    try:
        file = requests.get(url, allow_redirects=True)
        # To connect to the link via http request
        if file.status_code == 200:
            print("Link is accessible")
            with open(path + "/" + filename, "wb") as f:
                # Writing the file as binary with the help of file method
                f.write(file.content)
                f.close()
                print("File is downloaded successfully")
        else:
            print("please enter the correct link")

    except requests.exceptions.HTTPError as errH:
        print("Http Error:", errH)
    except requests.exceptions.ConnectionError as errC:
        print("Error Connecting:", errC)
    except requests.exceptions.Timeout as errT:
        print("Timeout Error:", errT)
    except requests.exceptions.RequestException as errE:
        print("oops: Something Else", errE)

if __name__ == "__main__":
    url = input("Enter the  file link:")
    filename = input("Enter the File Name along with format:")
    # To read the local directory where the file will be stored
    path = str(os.getcwd())
    download_file_from_google_drive(url, filename)
