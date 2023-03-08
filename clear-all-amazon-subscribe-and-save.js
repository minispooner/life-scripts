/*
Description:
  This script clears out all your Amazon Subscribe and Save items.

Usage:
  - login to amazon in a browser
  - go to your account > subscribe and save > subscriptions
  - open browser tools JS console
  - run the below code
*/
items = document.getElementsByClassName("subscription-card");
let i = 0;
let id = "";
let url = "";
let xhttp = new XMLHttpRequest();
const iteration_len = items.length;

while (i < iteration_len) {
    console.log('Deleting ' + i);
    id = items[i].getAttribute("data-subscription-id");
    url = "https://www.amazon.com/auto-deliveries/ajax/cancelSubscriptionAction?deviceType=desktop&deviceContext=web&actionType=cancelSubscription&subscriptionId=" + id
    xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, true);
    xhttp.send();
    i++;
};
