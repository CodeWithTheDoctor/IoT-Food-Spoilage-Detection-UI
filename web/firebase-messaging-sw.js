importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-messaging-compat.js');


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
    const notificationTitle = payload.data.title;
    const notificationOptions = {
        body: payload.data.body,
        title: payload.data.title,
        icon: 'https://cdn-icons-png.freepik.com/512/7586/7586916.png'
    };

    self.registration.showNotification(notificationTitle, notificationOptions);
});