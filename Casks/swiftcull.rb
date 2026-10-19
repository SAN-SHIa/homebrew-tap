cask "swiftcull" do
  version "4.1.2"
  sha256 "372514a82252ee1a08fab61a2ff5faa3d1cd5ff3039a1862cf1d44d10c05518f"

  url "https://github.com/SAN-SHIa/SwiftCull/releases/download/v#{version}/SwiftCull.dmg"
  name "SwiftCull"
  desc "Native photo browsing, culling, and watermarking tool"
  homepage "https://github.com/SAN-SHIa/SwiftCull"

  livecheck do
    url :url
    strategy :github_latest
  end

  depends_on arch: :arm64
  depends_on macos: :sonoma

  app "SwiftCull.app"

  caveats <<~EOS
    SwiftCull is currently ad-hoc signed and is not notarized by Apple.
    macOS may block the first launch. Review the release source and use
    System Settings > Privacy & Security if you decide to allow the app.
  EOS
end
