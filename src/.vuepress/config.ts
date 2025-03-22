import { defineUserConfig } from "vuepress";
import { hopeTheme } from "vuepress-theme-hope";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "知识库",
  description: "江苏理工学院知识文档",

  theme

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
