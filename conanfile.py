# tidy-html5 conand recipe 
# as used by https://github.com/zethon/Owl

from conans import ConanFile, CMake, tools

class LibtidyConan(ConanFile):
    name = "tidy-html5"
    version = "5.7.28"
    url = "https://github.com/htacg/tidy-html5"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    scm = {"revision": "d1b906991a7587688d384b648c55731f9be52506",
           "type": "git",
           "url": "https://github.com/htacg/tidy-html5.git",
           "subfolder": "source"}

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="source")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="source/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]