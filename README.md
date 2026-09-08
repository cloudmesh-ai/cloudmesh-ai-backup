# Cloudmesh AI Backup

**Cloudmesh AI Backup** is a specialized utility within the Cloudmesh AI ecosystem designed to provide robust backup and recovery capabilities for AI infrastructure, configurations, and datasets.

## Overview

In the complex environment of AI clusters and HPC nodes, maintaining consistent backups of configuration files, model weights, and orchestration scripts is critical. `cloudmesh-ai-backup` provides a standardized way to execute backup operations across the ecosystem.

## Key Features

- **Integrated CLI**: Seamlessly integrates with the `cmc` (Cloudmesh AI Command) interface.
- **Ecosystem Aware**: Designed to work with other `cloudmesh-ai-*` tools to ensure all critical AI infrastructure components are captured.
- **Consistent Interface**: Follows the standardized Cloudmesh AI patterns for logging, I/O, and configuration.

## Installation

### 1. Install the Core CLI
Ensure you have the central orchestrator installed:
```bash
pip install cloudmesh-ai-cmc
```

### 2. Install the Backup Tool
```bash
pip install cloudmesh-ai-backup
```

## Usage

The backup functionality is exposed as a command within the `cmc` utility.

### Basic Backup
To execute the backup process:
```bash
cmc backup
```

## Development

If you are contributing to the backup tool, use the provided `Makefile` for common tasks:

- **Install in editable mode**:
  ```bash
  make install
  ```
- **Run Tests**:
  ```bash
  make test
  ```
- **Build Documentation**:
  ```bash
  make doc
  ```

## Documentation

For detailed technical specifications and API references, please visit the official documentation site:
👉 **[Cloudmesh AI Backup Docs](https://cloudmesh-ai.github.io/cloudmesh-ai-backup/)**

## Contribution

Contributions are welcome! Please follow the standard Cloudmesh AI development guidelines. For more information, refer to the [Cloudmesh AI Manual](https://cloudmesh-ai.github.io/cloudmesh-ai-manual/).
