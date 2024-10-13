importScripts('https://www.gstatic.com/firebasejs/10.14.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.14.1/firebase-messaging-compat.js');


const firebaseConfig = {
    apiKey: "AIzaSyB6bDJ8CVYJGSknBtuDPpARfq7FYPWXtNI",
    authDomain: "superchat-a933e.firebaseapp.com",
    projectId: "superchat-a933e",
    storageBucket: "superchat-a933e.appspot.com",
    messagingSenderId: "292696901282",
    appId: "1:292696901282:web:e99fdfb6c880ee157e79fb"
};
firebase.initializeApp(firebaseConfig)
const messaging = firebase.messaging()

messaging.onBackgroundMessage((payload) => {
    console.log(
        '[firebase-messaging-sw.js] Received background message ',
        payload
    );
    // Customize notification here
    const notificationOptions = {
        body: payload.data.body,
        icon: 'noti_icon.png',
        type: json
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
    self.addEventListener('install', (event) => {
    console.log('Installed');
});

self.addEventListener('activate', (event) => {
    console.log('Activated');
});

self.addEventListener('fetch', (event) => {
    console.log('Fetch request');
});

});