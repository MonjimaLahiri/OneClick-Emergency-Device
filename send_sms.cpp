//translation of the send sms function in cpp from python
#include <iostream>
#include <string>
#include <curl/curl.h>

const std::string accountID = "AC7e4ee9bae71a3d04c7f5d3cc9f9f4440";
const std::string authToken= "b43b1b4af2a31dbcac673c5d3a270c15";
const std::string message="SOS: SA Victim";
const std::string twolioPhoneNumber ="+18777193732";
const std::string recipientPhoneNumber = "+recipient_phone_number"; //replace with recipient phone number

void send_sms(){
    CURL* curl;
    CURLcode res;

    std::string url = "https://api.twilio.com/2010-04-01/Accounts/"+accountID+"/Messages.json";
    std::string postFields = "Body="+message+"&From="+twolioPhoneNumber+"&To="+recipientPhoneNumber;
    curl = curl_easy_init();
    if(curl){
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

        curl_easy_setopt(curl, CURLOPT_USERNAME, accountID.c_str());
        curl_easy_setopt(curl, CURLOPT_PASSWORD, authToken.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postFields.c_str());

        res=curl_easy_perform(curl)

        if(res!=CURLE_OK) {
            std::cerr<<"failed to Send SMS: " << curl_easy_strerr(res) << std::endl;
        }
        else {
            std::cout << "SMS sent sucessfully"<<std::endl;
        }
        curl_easy_cleanup(curl)
    }
    else {
        std::cerr<<"Failed to intitialize cURL" << std::endl
    }
}

int main(){
    send_sms()
    return 0;
}