# Junhao Wei · AcadHomepage

本主页实际使用 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 开源模板，与 Yuhuan Lu 主页同源。模板的布局、字体、圆形头像、响应式侧栏与导航均保留，使用 Jekyll 构建。

目标仓库：`JunhaoWei-mpu/JunhaoWei-mpu.github.io`

目标网址：<https://JunhaoWei-mpu.github.io/>

## 本地预览

本机已构建的页面位于 `_site/`。运行：

```bash
bash 打开主页.sh
```

脚本启动本地 HTTP 预览并直接调用浏览器，默认地址为 <http://127.0.0.1:4000/>，端口被占用时会选择下一个可用端口。新版是 Jekyll 模板，根目录不再放旧的静态 `index.html`。不要直接用文件协议打开 `_site/index.html`，因为模板资源使用站点路径。

开发时自动构建、刷新：

```bash
bundle install
bash run_server.sh
```

需要 Ruby、Bundler 和 Ruby 开发头文件。推荐 Ruby 3.3。若 `bundle` 不在 PATH，`run_server.sh` 会尝试用户的 gem 安装目录。本机依赖安装于 `~/.cache/acadhomepage-bundle`；`.bundle/config` 为本机配置，不提交。

手动构建及检查：

```bash
bundle exec jekyll build
python3 scripts/check_site.py
python3 scripts/package_site.py
```

## 发布到 GitHub Pages

源代码已针对 `JunhaoWei-mpu.github.io` 配置。仓库现有历史应保留，不能重新初始化远程或强制覆盖历史。

1. 将本项目源代码提交到仓库 `main` 分支。不要提交 `_site/`、本机依赖、原始简历和照片、ZIP 压缩包。
2. 打开仓库 **Settings → Pages → Build and deployment**，Source 选择 **GitHub Actions**。
3. `.github/workflows/pages.yml` 会安装依赖、构建、检查并部署 `_site/`。如果首次配置时构建未触发，在 Actions 页面手动运行 **Build and deploy academic homepage**。
4. 等待工作流成功，再访问目标网址。

参见 [GitHub Pages 自定义工作流文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。

## 日常维护

- `_config.yml`：姓名、邮箱、Google Scholar、GitHub、机构等信息。
- `_pages/about.md`：简介、News、奖项、教育经历、Reviewer、PC。
- `_data/navigation.yml`：顶部导航。
- `_data/publications.json`：论文记录，修改后由 Jekyll 自动生成论文列表。
- `_includes/publications.html`：普通论文列表格式与筛选规则。
- `assets/portrait.jpg`：头像，同时用作浏览器标签页的小图标。
- `_sass/_custom.scss`：少量定制样式。其余排版使用原始模板。

中文姓名、简历入口及简历 PDF 均不发布。原始简历和照片仍在本机保留，已从 Jekyll 输出与 Git 提交中排除。

## 论文规则

以作者于 2026-09-20 粘贴的 Google Scholar 列表为准，共 27 条有正式期刊或会议名称的论文。已接收的标注 **Accepted**；不显示 Highlights、框架图或贡献描述。`status` 为 `published` 或 `accepted`，正式出版后可修改状态并补充 DOI 与卷页。

排除明确标为 arXiv / Preprints / SSRN 的 9 条记录，以及没有期刊或会议信息的 ARIES-Mission、MOBI Depth。原始 Scholar 列表省略的作者显示为 `et al.`，不猜测姓名；AIIPCC 2025 条目按 Scholar 年份归入 2026。

已核实 DOI 的标题链接到出版社，其他标题使用 Scholar 标题检索。近期接收但未提供题目的论文只在 News 中保留数量。

## 交付与来源

- `homepage-source.zip`：可维护的 Jekyll 源码，建议用于 GitHub 仓库。
- `homepage-ready.zip`：已经构建的静态成品，供静态服务器托管；内含 `.nojekyll`，不是 Jekyll 源码。
- 迁移前的旧页面已备份到本目录之外：`../homepage-before-acadhomepage-20260920.zip`。
- `LICENSE` 保留 AcadHomepage 的 MIT 许可证；具体上游版本和改动说明见 `TEMPLATE.md`。
