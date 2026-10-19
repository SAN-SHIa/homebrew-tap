# SwiftCull Homebrew Tap

SwiftCull 的 Homebrew Cask 分发仓库，由 [SwiftCull](https://github.com/SAN-SHIa/SwiftCull) 作者维护。

## 安装

支持 **Apple Silicon（M 系列芯片）及 macOS 14 Sonoma 或更高版本**。当前发布包不支持 Intel Mac。

```bash
brew tap SAN-SHIa/tap
brew install --cask SAN-SHIa/tap/swiftcull
```

## 升级与卸载

```bash
brew update
brew upgrade --cask SAN-SHIa/tap/swiftcull
brew uninstall --cask SAN-SHIa/tap/swiftcull
```

卸载不会删除个人照片、评分、裁剪记录或预设。

当前应用使用临时签名，尚未经过 Apple 公证，首次打开可能被 macOS 拦截。请确认来自官方发布，再通过“系统设置 → 隐私与安全性”决定是否允许打开。此 Tap 不修改 Gatekeeper 设置。

## 维护

安装包直接来自官方 GitHub Releases，Cask 使用固定版本和 SHA-256 校验值。

在本仓库的 Actions 页面手动运行 **Update SwiftCull**，可读取上游最新稳定版本、下载验证安装包并更新 Cask。运行前须在 `commit_message` 输入框中明确填写并确认完整提交信息，例如 `chore: update SwiftCull to v4.1.3`。工作流会校验信息与实际版本一致，仅在版本或校验值变化时提交；不需要额外的个人访问令牌。

本地也可运行以下命令，再检查差异并提交：

```bash
python3 scripts/update-cask.py
brew style Casks/swiftcull.rb
```

`livecheck` 用于检测上游版本，实际安装版本以 Cask 中的 `version` 为准。每次更新仍需确认安装包架构和最低系统要求未发生变化。

软件问题请反馈至 [SwiftCull Issues](https://github.com/SAN-SHIa/SwiftCull/issues)。
