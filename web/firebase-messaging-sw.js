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
firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);

    // Check if payload.data and payload.data.notification exist
    if (payload.data) {
        const notificationTitle = payload.data.title;
        const body = payload.data.body;

        // Customize notification here
        const notificationOptions = {
            body: body,
            icon: 'https://foodspoilage.developerash.net/noti_icon.png',
            image: 'https://i.imgur.com/FnTifxX.png',
            data: {
                url: 'https://foodspoilage.developerash.net/' // Add URL to data property
            }
        };

        self.registration.showNotification(notificationTitle, notificationOptions);
    } else {
        console.error('Notification payload is missing data or notification property');
    }
});

self.addEventListener('notificationclick', (event) => {
    console.log('[firebase-messaging-sw.js] Notification click Received.');

    event.notification.close();

    // Open the URL specified in the notification data
    event.waitUntil(
        clients.openWindow(event.notification.data.url)
    );
});

self.addEventListener('install', (event) => {
    console.log('Installed');
});

self.addEventListener('activate', (event) => {
    console.log('Activated');
});

self.addEventListener('fetch', (event) => {
    console.log('Fetch request');
});