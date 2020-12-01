<template>
  <div class="font-bold leading-none font-mono" style="line-height: 0.9">
    <h1 :style="{ 'font-size': emotions.angry * 1000 + 'px' }">
      Angry
    </h1>
    <h1 :style="{ 'font-size': emotions.disgust * 1000 + 'px' }">
      Disgust
    </h1>
    <h1 :style="{ 'font-size': emotions.scared * 1000 + 'px' }">
      Scared
    </h1>
    <h1 :style="{ 'font-size': emotions.happy * 1000 + 'px' }">
      Happy
    </h1>
    <h1 :style="{ 'font-size': emotions.sad * 1000 + 'px' }">
      Sad
    </h1>
    <h1 :style="{ 'font-size': emotions.surprised * 1000 + 'px' }">
      Surprised
    </h1>
    <h1 :style="{ 'font-size': emotions.neutral * 1000 + 'px' }">
      Neutral
    </h1>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      emotions: "",
    };
  },
  sockets: {
    connect: function() {
      console.log("socket connected");
    },
    serverToClient: function(text) {
      this.emotions = text;
      //console.log(text);
    },
  },
  methods: {
    sendMessage() {
      if (this.activeMessage) {
        let message = this.textToMessage(this.activeMessage, true);
        this.messages.push(message);
        this.$socket.emit("clientToServer", message);
        this.activeMessage = "";
      }
    },
  },
};
</script>
