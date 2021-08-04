chrome.runtime.onInstalled.addListener(function() {
  var menuItem = {
    "id": "catchURL",
    "title": "Sherlock",
    "contexts": ["all"]
    };

  chrome.contextMenus.create(menuItem);
});

var serverhost = 'http://127.0.0.1:8000';

chrome.contextMenus.onClicked.addListener(function(clickData, tab){
    if(clickData.menuItemId == "catchURL"){
        chrome.tabs.query({active: true, lastFocusedWindow: true}, function(tabs){
            newsURL = tabs[0].url || clickData.framUrl || clickData.pageUrl;
            var url = serverhost + '/sherlock/predict_news/?news_url='+ newsURL;
            fetch(url)
            .then(response => response.json())
            .then(data => {
                var notifOptions = {
                    type: "basic",
                    iconUrl: "icon48.png",
                    title: "Sherlock's prediction",
                    message: data.prediction
                };
                chrome.notifications.create('SherlockNotif', notifOptions);
            })
        });
    }
});
