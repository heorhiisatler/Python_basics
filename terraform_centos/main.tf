terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = ">= 2.7"
    }
  }
}

provider "proxmox" {
    pm_api_url = "https://192.168.5.251:8006/api2/json"
    pm_tls_insecure = true
    pm_api_token_id = var.pm_api_token_id
    pm_api_token_secret = var.pm_api_token_secret


}

variable "ssh_key" {}
variable "pm_api_token_id" {}
variable "pm_api_token_secret" {}
variable "vm_number" {}
variable "name" {}


resource "proxmox_vm_qemu" "proxmox_vm" {
  count             = var.vm_number
  name              = "${var.name}-${count.index}"
  target_node       = "pve2"
  clone             = "centos-cloud-init"
  os_type           = "cloud-init"
  cores             = 1
  sockets           = "1"
  cpu               = "host"
  memory            = 2048
  scsihw            = "virtio-scsi-pci"
  bootdisk          = "scsi0"
  disk {
    size            = "8G"
    type            = "scsi"
    storage         = "local-lvm"
  }
  network {
    model           = "virtio"
    bridge          = "vmbr0"
  }
  lifecycle {
    ignore_changes  = [
      network,
    ]
  }

# Cloud Init Settings
  ipconfig0  = "ip=192.168.5.3${count.index + 3}/24,gw=192.168.5.24"
  nameserver = "192.168.5.248"
  sshkeys = <<EOF
  ${var.ssh_key}
  EOF
}