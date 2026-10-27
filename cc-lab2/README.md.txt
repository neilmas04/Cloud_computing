# Local Kubernetes Cluster: Deployment, Scaling, and Self-Healing

## Overview
This project demonstrates the deployment of a local, multi-node Kubernetes cluster using Docker and `kind` (Kubernetes IN Docker). It covers the practical implementation of core Kubernetes concepts, including container orchestration, application deployment, declarative scaling, and automated self-healing.

## My Understanding of the Core Concepts
Through this experiment, I explored several key Kubernetes mechanisms:
* **Cluster Architecture (`kind`)**: Instead of needing separate physical or virtual machines, `kind` allows us to run Kubernetes nodes as individual Docker containers. This setup mimics a production environment locally.
* **Control Plane vs. Worker Nodes**: The Control Plane acts as the brain (managing state, scheduling, and API requests), while the Worker Nodes are the muscles (running the actual application workloads).
* **Deployments and Pods**: Rather than running containers directly, Kubernetes wraps them in Pods. Deployments act as a declarative blueprint, telling Kubernetes exactly how many Pods should be running at any given time.
* **Self-Healing Mechanism**: Kubernetes constantly monitors the state of the cluster. If a Pod is deleted or crashes, the controller manager detects the variance from the desired state and immediately spins up a replacement Pod to maintain the required replica count.

## Steps Taken to Complete the Lab

**1. Environment Setup & Troubleshooting**
* Configured a dual-OS development environment by enabling SVM (Hardware Virtualization) in the BIOS and configuring Windows Subsystem for Linux (WSL 2).
* Resolved hypervisor conflicts to successfully run Docker Desktop on Windows.
* Installed the required CLI tools: `kubectl` for cluster interaction and `kind` for cluster provisioning.

**2. Cluster Provisioning**
* Authored a YAML configuration file (`kind-config.yaml`) defining a 3-node architecture.
* Executed the cluster build, resulting in one Control Plane node and two Worker nodes running as isolated Docker containers.

**3. Application Deployment**
* Deployed an NGINX web application using the `kubectl create deployment` command.
* Specified 3 initial replicas and verified that the Kubernetes scheduler distributed the NGINX Pods evenly across the two worker nodes.

**4. Scaling and Self-Healing Validation**
* **Scaling**: Dynamically scaled the deployment from 3 to 6 replicas using the `kubectl scale` command, observing the seamless rollout of new Pods without downtime.
* **Self-Healing**: Intentionally deleted a running Pod to simulate a node failure or application crash. Verified that the Kubernetes control loop instantly detected the missing Pod and spun up a new replacement to restore the desired state of 6 replicas.