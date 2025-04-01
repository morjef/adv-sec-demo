import unittest
import os
import tempfile

class GitHubDependencyTests(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_path = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_file(self, filename, content):
        file_path = os.path.join(self.repo_path, filename)
        with open(file_path, "w") as f:
            f.write(content)

    def _simulate_maven_check(self, pom_content):
        self._create_file("pom.xml", pom_content)
        vulnerable_deps = []
        if "log4j:log4j:1.2.17" in pom_content:
            vulnerable_deps.append("log4j:log4j:1.2.17")  # Simulate known log4j vulnerability
        return vulnerable_deps

    def _simulate_flask_check(self, requirements_content):
        self._create_file("requirements.txt", requirements_content)
        vulnerable_deps = []
        if "Flask==2.0.0" in requirements_content:
            vulnerable_deps.append("Flask==2.0.0")  # Simulate a known vulnerable Flask version
        return vulnerable_deps

    def _simulate_dotnet_check(self, csproj_content):
        self._create_file("Project.csproj", csproj_content)
        vulnerable_deps = []
        if '<PackageReference Include="Newtonsoft.Json" Version="12.0.0" />' in csproj_content:
            vulnerable_deps.append("Newtonsoft.Json 12.0.0") #Simulate vulnerable Newtonsoft.Json version.
        return vulnerable_deps

    def test_maven_vulnerability(self):
        pom_content = """
        <project>
            <dependencies>
                <dependency>
                    <groupId>log4j</groupId>
                    <artifactId>log4j</artifactId>
                    <version>1.2.17</version>
                </dependency>
            </dependencies>
        </project>
        """
        vulnerable_deps = self._simulate_maven_check(pom_content)
        self.assertEqual(vulnerable_deps, ["log4j:log4j:1.2.17"])

    def test_flask_vulnerability(self):
        requirements_content = "Flask==2.0.0"
        vulnerable_deps = self._simulate_flask_check(requirements_content)
        self.assertEqual(vulnerable_deps, ["Flask==2.0.0"])

    def test_dotnet_vulnerability(self):
        csproj_content = """
        <Project Sdk="Microsoft.NET.Sdk">
            <ItemGroup>
                <PackageReference Include="Newtonsoft.Json" Version="12.0.0" />
            </ItemGroup>
        </Project>
        """
        vulnerable_deps = self._simulate_dotnet_check(csproj_content)
        self.assertEqual(vulnerable_deps, ["Newtonsoft.Json 12.0.0"])

    def test_clean_maven(self):
        pom_content = """
        <project>
            <dependencies>
                <dependency>
                    <groupId>log4j</groupId>
                    <artifactId>log4j</artifactId>
                    <version>2.17.0</version>
                </dependency>
            </dependencies>
        </project>
        """
        vulnerable_deps = self._simulate_maven_check(pom_content)
        self.assertEqual(vulnerable_deps, [])

    def test_clean_flask(self):
        requirements_content = "Flask>=2.3.0"
        vulnerable_deps = self._simulate_flask_check(requirements_content)
        self.assertEqual(vulnerable_deps, [])

    def test_clean_dotnet(self):
        csproj_content = """
        <Project Sdk="Microsoft.NET.Sdk">
            <ItemGroup>
                <PackageReference Include="Newtonsoft.Json" Version="13.0.1" />
            </ItemGroup>
        </Project>
        """
        vulnerable_deps = self._simulate_dotnet_check(csproj_content)
        self.assertEqual(vulnerable_deps, [])

if __name__ == '__main__':
    unittest.main()
