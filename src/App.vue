<template>
  <div class="w-screen h-screen flex items-center py-48">
    <div class="flex flex-col justify-between w-1/4 h-64 min-h-full mx-16 p-4 ">
      <div class="overflow-y-auto px-4 w-full mb-4" id="chatWindow">
        <div
          v-for="(message, index) in messages"
          :key="index"
          class="flex"
          v-bind:class="{
            'flex-row-reverse': message.client
          }"
        >
          <div>
            <p class="text-xs ml-auto font-bold text-gray-600">
              {{ message.time }}
            </p>
            <p
              class="text-white px-4 py-2 bg-blue-900 shadow-lg rounded-2xl"
              v-bind:class="{
                'rounded-tr-none': message.client,
                'rounded-tl-none': !message.client
              }"
            >
              {{ message.text }}
            </p>
          </div>
          <div class="w-full h-full"></div>
        </div>
      </div>
      <div class="self-end w-full px-4 flex justify-between space-x-2 ">
        <input
          v-model="activeMessage"
          v-on:keyup.enter="sendMessage"
          placeholder="Send message"
          type="text"
          class="bg-gray-900 w-full shadow-lg rounded-full px-4 py-2 text-white focus:outline-none "
        />
        <button
          @click="sendMessage"
          class="bg-red-500 px-4 py-2 rounded-full font-bold text-white shadow-lg focus:outline-none "
        >
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      activeMessage: "",
      messages: []
    };
  },
  sockets: {
    connect: function() {
      console.log("socket connected");
    },
    serverToClient: function(text) {
      this.messages.push(this.textToMessage(text, false));
      this.scrollToBottom();
    }
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
    textToMessage(text, client) {
      return {
        client: client,
        text: text,
        time: new Date().toTimeString().split(" ")[0]
      };
    },
    scrollToBottom() {
      var element = document.getElementById("chatWindow");
      element.scrollTop = element.scrollHeight;
    }
  }
};
</script>
