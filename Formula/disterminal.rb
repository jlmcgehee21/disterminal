class Disterminal < Formula
  include Language::Python::Virtualenv

  desc "Plot scipy stats distributions in your terminal"
  homepage "https://github.com/jlmcgehee21/disterminal"
  url "https://github.com/jlmcgehee21/disterminal/archive/v0.2.0.tar.gz"
  sha256 "1ec12e8e1bca7bdcc82f20209b1a1c66fa61eb48a8871078cadbcf6bc128d00d"

  depends_on "python"
  depends_on "gnuplot"

  resource "numpy" do
    url "https://files.pythonhosted.org/packages/0b/66/86185402ee2d55865c675c06a5cfef742e39f4635a4ce1b1aefd20711c13/numpy-1.14.2.zip"
    sha256 "facc6f925c3099ac01a1f03758100772560a0b020fb9d70f210404be08006bcb"
  end

  resource "scipy" do
    url "https://files.pythonhosted.org/packages/d0/73/76fc6ea21818eed0de8dd38e1e9586725578864169a2b31acdeffb9131c8/scipy-1.0.0.tar.gz"
    sha256 "87ea1f11a0e9ec08c264dc64551d501fa307289460705f6fccd84cbfc7926d10"
  end

  resource "click" do
    url "https://files.pythonhosted.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/click-6.7.tar.gz"
    sha256 "f15516df478d5a56180fbf80e68f206010e6d160fc39fa508b65e035fd75130b"
  end

  resource "fabulous" do
    url "https://files.pythonhosted.org/packages/53/2d/5750798dbb1cd3029c17b6f7456f79948b15f63e4781ffa0be8cf35cfc22/fabulous-0.3.0.tar.gz"
    sha256 "54040da01d7ce1e937fc4b61d265e872b007463bea411a3a5762f4d6ee55c312"
  end


  def install
    virtualenv_install_with_resources
  end

  test do
    system "disterminal norm pdf 0 1 --color 'green'"
  end
end
