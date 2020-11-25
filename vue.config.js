module.exports = {
  pluginOptions: {
    prerenderSpa: {
      registry: undefined,
      renderRoutes: ["/"],
      useRenderEvent: false,
      headless: true,
      onlyProduction: true
    }
  },
  pwa: {
    name: "Chat",
    themeColor: "#4DBA87",
    msTileColor: "#000000",
    appleMobileWebAppCapable: "yes",
    appleMobileWebAppStatusBarStyle: "black"
  }
};
