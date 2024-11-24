# Exposor Contributor's Guide

Thank you for your interest in contributing to Exposor! Your contributions help improve the tool and expand its capabilities. This guide explains how to add new YAML files for `intels`, how to use the `vulners-api.py` script to generate vulnerabilities, and how to follow the contribution process.

---

## 1. Adding New YAML Files for Intels

### Purpose
The `intels` directory contains YAML files used for detecting technologies and vulnerabilities. New YAML files should:
- Be well-structured and follow the existing format.
- Include accurate and valid queries for supported platforms (e.g., Shodan, Fofa, ZoomEye, Censys).
- Be tested to ensure they work correctly.

### Directory Structure
The repository is organized to keep YAML files structured and easy to navigate. Below is an overview of the directory structure:

```text
exposor/                               
├── intels/                                               # Folder for intelligence YAML files
│   ├── technology_intels/                                # Technology-specific YAML files 
│   │   ├── vendor_name/                                  # Vendor name folder
│   │   │   ├── product_name/                             # Product name folder
│   │   │   │   ├── vendor_product.yaml   <––– Example technology YAML
│   └── vulnerability_intels/                             # Vulnerability-specific YAML files
│   │   ├── vendor_product_cves.yaml      <––– Example vulnerability YAML
└── ...
```

- **`technology_intels/`**: Contains YAML files for detecting specific technologies or platforms. Files are organized by `vendor_name/product_name/vendor_product.yaml`.
- **`vulnerability_intels/`**: Contains YAML files for tracking vulnerabilities (e.g., CVEs) generated using the `vulners-api.py` script.


For example:
- YAML file for **cpe:2.3:a:apache:activemq** should be placed in:
  ```
  exposor/intels/technology_intels/apache/activemq/apache_activemq.yaml
  ```

### Minimum Requirements for YAML Files
Every YAML file must include the following fields:
- **`cpe`**: The name of the technology or vulnerability.
- **`description`**: A brief description of the detection.
- **`queries`**: The platform-specific queries.

#### Example YAML Template:
```yaml
info:
  author: exposor
  cpe: cpe:2.3:a:3cx:3cx:*:*:*:*:*:*:*:*
  description: Detection of 3cx 3cx
  version: '1.0'
queries:
  censys:
  - services.http.response.html_title:"3CX Phone System Management Console"
  fofa:
  - title="3CX Phone System Management Console"
  shodan:
  - http.title:"3CX Phone System Management Console"
  zoomeye:
  - title:"3CX Phone System Management Console"
```

---

## 2. Generating Vulnerabilities for CPEs

You can run the `vulners-api.py` script against your YAML file to generate a list of vulnerabilities for related CPEs.

### Steps to Generate Vulnerabilities:
1. **Place Your YAML File**:
   - Ensure your YAML file is located in the appropriate directory (e.g., `intels/technology_intels/apache/activemq/apache_activemq.yaml`).

2. **Run the `vulners-api.py` Script**:
   - Use the following command to generate vulnerabilities:
     ```bash
     python3 scripts/vulners-api.py intels/technology_intels/<vendor>/<product>/<vendor_product>.yaml
     ```
   - Example for Apache ActiveMQ:
     ```bash
     python3 scripts/vulners-api.py intels/technology_intels/apache/activemq/apache_activemq.yaml
     ```

3. **Output File**:
   - The script will save the vulnerabilities in:
     ```
     exposor/intels/vulnerability_intels/<vendor_product>_cves.yaml
     ```
   - Example:
     ```
     exposor/intels/vulnerability_intels/apache_activemq_cves.yaml
     ```

4. **Validate the Output**:
   - Ensure the generated file is saved correctly in `vulnerability_intels/` and includes all relevant CVEs.

---

## 3. Steps to Contribute a YAML File

### Workflow for Adding a New YAML File:
1. **Fork the Repository**:
   - Fork the Exposor repository to your GitHub account.

2. **Clone Your Fork**:
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/abuyv/exposor.git
     cd exposor
     ```

3. **Create a New Branch**:
   - Create a branch for your contribution:
     ```bash
     git checkout -b feature/add-<vendor>-<product>
     ```

4. **Add Your YAML File**:
   - Create the YAML file in the appropriate folder:
     ```bash
     mkdir -p intels/<vendor>/<product>
     touch intels/<vendor>/<product>/<vendor_product>.yaml
     ```

5. **Run `vulners-api.py`** (Optional but Recommended):
   - Generate vulnerabilities for your CPEs using the `vulners-api.py` script as described above.

6. **Test Your Changes**:
   - Ensure there are no syntax errors in your YAML file.

7. **Commit Your Changes**:
   - Commit the changes with a clear message:
     ```bash
     git add .
     git commit -m "Add detection for <Vendor Product>"
     ```

8. **Push Your Branch**:
   - Push the branch to your fork:
     ```bash
     git push origin feature/add-<vendor>-<product>
     ```

9. **Open a Pull Request**:
   - Open a pull request from your fork to the main repository.

---

## 4. Reviewing Pull Requests

When you submit a pull request:
- A maintainer will review your YAML file to ensure it follows the guidelines.

---

## 5. Reporting Issues

If you encounter any issues with the project, please open an issue with the following details:
- A clear title.
- A description of the issue.
- Steps to reproduce the problem.
- Logs or screenshots, if applicable.

---

## 6. Additional Resources
- Refer to the [README.md](README.md) for an overview of the project.

Thank you for contributing to Exposor!
