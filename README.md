# SpringBootProjectInitializer

SpringBootProjectInitializer is a tool to automate the setup and initialization of Spring Boot projects. It uses a configuration file to generate a new Spring Boot project with specified dependencies, and sets up necessary services like PostgreSQL, MongoDB, Kafka, Redis, Keycloak/Spring Authorization Server, Jenkins, GitHub Actions, and more.

## Dependencies

This project uses the following dependencies:

- Spring Boot
- Spring Cloud Stream
- Python
- Gradle
- Ansible
- Terraform

## Getting Started

To use this tool, you need to:

1. Clone this repository
2. Define your project configuration in a JSON or YAML file
3. Run the Python script to generate the project and set up the services
4. Use Ansible for configuration management
5. Use Terraform for infrastructure provisioning
6. Set up CI/CD pipelines with GitHub Actions and Jenkins

## Configuration

The configuration file should specify the technologies to be used, any specific settings for those technologies, and the structure of the project (e.g., which modules to include, what APIs to generate, etc.).

Here's an example configuration:

```json
{
  "language": "java",
  "type": "gradle-project",
  "bootVersion": "2.5.4",
  "baseDir": "myproject",
  "groupId": "com.example",
  "artifactId": "myproject",
  "name": "myproject",
  "description": "Demo project for Spring Boot",
  "packageName": "com.example.myproject",
  "packaging": "jar",
  "javaVersion": "11",
  "dependencies": "web,data-jpa,h2,cloud-stream"
}
```

## Contributing
Contributions are welcome! Please read the contributing guidelines first.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
