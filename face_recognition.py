import requests

import base64

import json



api_credentials={

    "Content-Type":"application/json",

    "app_id":"75f5edf9",

    "app_key":"ba0eadb825eddeb58d420e08bad09300"

}



url="https://api.kairos.com/"



def _extract_base64_contents(file):

    with open(file, 'rb') as fp:

        image = base64.b64encode(fp.read()).decode('ascii')

    return image



def post(image_link,identifier):

    payload={

        "image":_extract_base64_contents(image_link),

        "subject_id":identifier,

        "gallery_name":"gallery"

    }

    response=requests.post(url+"enroll",json=payload,headers=api_credentials).json()
    print "\n Detected attributes of New user\n"
    print ("Gender : ",response["images"][0]["attributes"]["gender"]["type"])
    print ("Age : ",response["images"][0]["attributes"]["age"])
    #print parsed.dumps(parsed,indent=4,sort_keys=True)



def recognize(image_link):

    payload={

        "image":_extract_base64_contents(image_link),

        "gallery_name":"gallery"

    }

    response=requests.post(url+"recognize",json=payload,headers=api_credentials)

    #with open("")

    gallery_response=response.json()
#    print gallery_response
    if 'Errors' in gallery_response:
	return -2
    
   # print gallery_response

    if gallery_response["images"][0]["transaction"]["status"]=="success":
	print "Image Detected with : ",gallery_response["images"][0]["transaction"]["confidence"]*100,"% Resemblance Factor"
        return gallery_response["images"][0]["transaction"]["subject_id"]
    print 'New User Found'
    return -1





def view_gallery():

    payload={

        "gallery_name": "gallery"

    }

    response=requests.post(url+"gallery/view",json=payload,headers=api_credentials)

    print(response.json())



def delete_user(identifier):

    payload={

        "subject_id":identifier,

        "gallery_name":"gallery"

    }

    response=requests.post(url+"gallery/remove_subject",json=payload,headers=api_credentials)

    print(response.json())



#post("http://media.kairos.com/kairos-elizabeth.jpg","1")

#post("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT7qBsj6rkafzGP6rTmZRpUYinKVI4HU8VXZjxG1TsthEoJmocl8UG6KKLT","2")

#print recognize("Crazy.png")

#print recognize("pp.jpg")



#post("Img.png","pawan")

#view_gallery()



#delete_user("5")
