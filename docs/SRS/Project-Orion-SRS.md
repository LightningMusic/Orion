# Project Orion

## Software Requirements Specification (SRS)

---

**Document ID:** ORION-SRS

**Version:** 0.1.0

**Status:** Draft

**Last Updated:** June 28, 2026

**Authors:**

* Elijah
* OpenAI ChatGPT

**Classification:** Internal Development

---

# Revision History

| Version | Date       | Author(s)              | Description                                 |
| ------- | ---------- | ---------------------- | ------------------------------------------- |
| 0.1.0   | 2026-06-28 | Elijah, OpenAI ChatGPT | Initial SRS created. Session One completed. |

---

# Table of Contents

1. Introduction
2. Project Overview
3. Vision
4. Goals
5. Project Scope
6. Non-Goals
7. Intended Audience
8. Terminology
9. Guiding Principles

---

# 1. Introduction

## 1.1 Purpose

Project Orion is a zero-touch infrastructure provisioning platform designed to automate the conversion of surplus and commodity computer hardware into managed virtualization infrastructure.

The project exists to eliminate repetitive deployment work while maintaining strict operator oversight for irreversible operations such as storage sanitization.

This document serves as the authoritative engineering specification for the Orion project.

No production feature shall be implemented before its behavior has been documented within this Software Requirements Specification.

---

## 1.2 Background

Building and maintaining virtualization clusters often requires repetitive manual configuration of hardware, firmware, operating systems, networking, and virtualization software.

Many organizations—and home lab operators—acquire large quantities of retired laptops and desktop systems that still possess significant computational value.

Preparing these systems manually is slow, error-prone, inconsistent, and difficult to reproduce.

Project Orion was conceived to standardize this process through automation while preserving operator control over destructive actions.

---

## 1.3 Project Mission

Project Orion exists to provide a safe, repeatable, operator-supervised provisioning platform for converting commodity computer hardware into managed Proxmox cluster resources.

The system shall minimize technician effort while maximizing deployment consistency, operational safety, and long-term maintainability.

---

# 2. Project Overview

Project Orion is not an operating system.

Project Orion is not a replacement for Proxmox.

Project Orion is an automated deployment platform responsible for preparing hardware for use within a Proxmox virtualization cluster.

The project provides tooling for:

* Hardware inspection
* Hardware validation
* Optional data recovery
* Secure storage preparation
* Automated Proxmox installation
* First-boot configuration
* Cluster enrollment
* Inventory registration
* Hardware benchmarking
* Deployment reporting

The deployment environment is distributed using bootable USB media.

The USB serves only as the deployment medium.

The Orion source code, documentation, build system, release process, and version control are maintained independently within the project's source repository.

---

# 3. Vision

The long-term vision of Project Orion is to allow a technician to transform supported computer hardware into production-ready virtualization resources using a standardized, repeatable deployment workflow.

When complete, Orion shall require minimal technician interaction after deployment has been authorized.

The deployment experience should resemble enterprise device provisioning platforms while remaining fully self-hosted and optimized for Proxmox environments.

The system shall scale from individual laboratory deployments to clusters consisting of many nodes without requiring architectural redesign.

---

# 4. Project Goals

Project Orion has the following primary objectives.

## G-001

Reduce deployment time for new cluster nodes.

---

## G-002

Standardize every deployed node.

---

## G-003

Reduce manual technician effort.

---

## G-004

Prevent accidental destruction of user data.

---

## G-005

Provide repeatable deployment workflows.

---

## G-006

Automatically configure supported hardware and operating system settings.

Examples include:

* Disable suspend on laptop lid closure.
* Configure supported battery charging limits.
* Configure supported power recovery settings.
* Apply deployment-specific operating system configuration.

---

## G-007

Automatically install and configure Proxmox VE.

---

## G-008

Automatically enroll deployed systems into the designated Proxmox cluster.

---

## G-009

Maintain centralized inventory for every deployed node.

---

## G-010

Provide complete deployment logs for auditing and troubleshooting.

---

## G-011

Support future expansion through a modular software architecture.

---

# 5. Project Scope

Version 1.0 of Project Orion includes the following major capabilities.

## Included

* Technician Console
* Hardware inspection
* Hardware validation
* Deployment readiness reports
* Optional customer data recovery
* Secure storage preparation
* Automated Proxmox installation
* Bootstrap automation
* Deployment Controller integration
* Automatic cluster enrollment
* Automatic inventory registration
* Hardware benchmarking
* Deployment reporting
* Configuration management
* Logging
* Software packaging
* USB deployment media generation

---

## Excluded

The following capabilities are outside the scope of Version 1.0.

* Cloud deployment
* Internet-hosted management
* Multi-cluster orchestration
* Windows deployment
* Consumer backup software
* Virtual machine management
* Container orchestration
* High-availability cluster management
* PXE network deployment

These capabilities may be evaluated in future releases.

---

# 6. Intended Audience

This document is intended for:

* Project developers
* System administrators
* AI coding assistants
* Software testers
* Technical reviewers
* Future project contributors

The document assumes familiarity with Linux, virtualization, networking, and software development practices.

---

# 7. Terminology

## Technician

The individual responsible for operating Orion.

---

## Technician Console

The interactive application launched from the deployment environment.

---

## Deployment Controller

The centralized service responsible for approving, configuring, registering, and provisioning new Orion nodes.

---

## Node

A successfully deployed Proxmox system managed by Orion.

---

## Inspection

The non-destructive examination of hardware prior to deployment.

---

## Recovery

The optional extraction of user data before destructive operations occur.

---

## Preparation

The operator-approved process responsible for securely sanitizing deployment storage.

---

## Provisioning

The automated installation and configuration of Proxmox.

---

## Bootstrap

The first-boot configuration process responsible for preparing a node for production operation.

---

## Inventory

The database of deployed systems maintained by the Deployment Controller.

---

## Deployment Session

The complete lifecycle beginning when Orion is launched and ending when deployment either succeeds or terminates.

---

# 8. Guiding Principles

Every engineering decision shall follow these principles.

---

## GP-001

Safety Before Automation

Automation shall never perform irreversible actions without explicit operator authorization.

---

## GP-002

Operator Supervision

Orion automates work.

Technicians authorize irreversible decisions.

---

## GP-003

Configuration Over Hardcoding

Deployment behavior shall be controlled through configuration rather than embedded source code values whenever practical.

---

## GP-004

Modular Design

Each subsystem shall perform one clearly defined responsibility.

---

## GP-005

Observability

Every significant operation shall be logged.

Deployment history shall be fully traceable.

---

## GP-006

Repeatability

Equivalent hardware deployed using equivalent configurations shall produce equivalent results.

---

## GP-007

Expandability

Future functionality shall be addable without requiring major architectural redesign.

---

## GP-008

Hardware Preservation

Supported hardware shall be configured to maximize long-term reliability.

Where technically possible Orion shall:

* Prevent suspend on lid closure.
* Configure supported battery charging thresholds.
* Configure supported firmware power settings.
* Report unsupported firmware features without failing deployment unless required for safe operation.

---

## GP-009

Centralized Management

Nodes shall receive deployment configuration from the Deployment Controller.

Installer media shall not contain permanently assigned deployment identities.

---

## GP-010

Documentation First

Every major feature shall be documented before implementation.

The Software Requirements Specification is the authoritative definition of project behavior.

---

# Session One Completion

The following project foundations have been established.

* Project purpose
* Project mission
* Project overview
* Long-term vision
* Goals
* Project scope
* Non-goals
* Intended audience
* Standard terminology
* Engineering principles

These sections define **what Orion is**.

Future revisions of this document will define **how Orion works**.

---

**End of Session One**

**Document Version:** 0.1.0
