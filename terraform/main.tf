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
    #pm_api_token_id = "tf_user@pve!terraform"
    #pm_api_token_secret  = "585dfaad-f6f3-4c75-acbc-5820a7fa4ea8"
    pm_api_token_id = var.pm_api_token_id
    pm_api_token_secret = var.pm_api_token_secret


}

variable "ssh_key" {
  default = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNsGvHB22PNhkpEEbgmpZBCBIq8KoGAMM+B1W2oaNhzK7nglte8wdttRthSUlaWB5aIfOCmspLRIaLPZ2Rg8/VkJA2xXPE5v9TIIQvkYOCKQ3xr7i4Uj0UFmGQX7YnFfs3dDBhLMObPU1bKz34NgwKW2xosidWFS8+xt0BmxBNqmTvwmr9YV0aqH0LJHyY2l7VYL6IVuGAViqrUvhPUXSeYRqylr2PVmrkOJMFOUYb76q9I4GF5wswJo75tFjSubqSuZ/IhMlhZvb+ZESE3jS4+ApMch3kD5hg719dG0RiwXaMHl4CzP+FfGy5JsAYi0mleuuh/d2F7H3MOS9ECsLAEAIhkRxWafA1j1n+OMuqHIeT8tJbFVQa/QQ3u1f9c/6Vy9SgC4V/nFCYcPuz8GevzgSG7Pd0C9ZNLPxb23gajTdTEvLEzk56/QeAIvoifLM+fNrZIaATutoC5ACzY/AJ5KyHl+Z/7dlmX1zwCnsRXYwMto5lrYcmVTsylg7xYb0= decepticon@control-srv.lan"
}

variable "pm_api_token_id" {}
variable "pm_api_token_secret" {}


resource "proxmox_vm_qemu" "proxmox_vm" {
  count             = 1
  name              = "ubuntu-vm-${count.index}"
  target_node       = "pve2"
  clone             = "ubuntu-cloud-init"
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
  ipconfig0  = "ip=192.168.5.3${count.index + 1}/24,gw=192.168.5.24"
  nameserver = "192.168.5.248"
  sshkeys = <<EOF
  ${var.ssh_key}
  EOF
}