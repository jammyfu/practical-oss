# 运行与基础设施

把应用送到机器上，并声明机器、网络和集群长什么样。

返回 [目录](../../README.md)。跨分类的名单在 [历史最高](../history.md) 和 [当前热度最高](../trending/2026-10-10/index.md)。

## 近两年的新默认

这一节只放本类里标了 `trending: yes` 的项目，按总星标从高到低。它不是今日、本周或本月的趋势榜。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [OpenBao](../../entries/infra/openbao.md) | 集中保管密钥、证书和加密能力，并作为 Vault 改许可后的开源延续。 | MPL-2.0 | 8,378 |
| [Incus](../../entries/infra/incus.md) | 在一台或一组机器上管理完整的 Linux 系统容器和虚拟机。 | Apache-2.0 | 6,367 |
| [bootc](../../entries/infra/bootc.md) | 用 OCI 容器镜像安装、启动和事务式更新整台 Linux 主机。 | MIT OR Apache-2.0 | 2,305（见正文） |
| [Karpenter](../../entries/infra/karpenter.md) | 按排不上的 Pod 直接申请和回收 Kubernetes 节点。 | Apache-2.0 | 2,219（见正文） |

## 历史最高

这一节是本类里的长期默认，按星标从高到低。星标不是采用率，镜像仓库尤其不能只看这个数字。

| 项目 | 它做什么 | 许可 | 星标 |
| --- | --- | --- | ---: |
| [Kubernetes](../../entries/infra/kubernetes.md) | 在多台机器上声明容器要跑几份、如何发现彼此，以及失败后如何拉回来。 | Apache-2.0 | 128,239 |
| [Docker](../../entries/infra/docker.md) | 把应用和依赖打成镜像，在本机或服务器上以容器方式重复运行。 | Apache-2.0 | 72,163（见正文） |
| [Ansible](../../entries/infra/ansible.md) | 用 SSH 和任务清单把多台机器配成声明的样子，目标机器上不必先装代理。 | GPL-3.0 | 70,948 |
| [K3s](../../entries/infra/k3s.md) | 用一个轻量发行版把 Kubernetes 跑在小集群、分支机构和边缘节点上。 | Apache-2.0 | 34,160（见正文） |
| [Podman](../../entries/infra/podman.md) | 在本机构建和运行容器，不依赖一个常驻的 Docker 守护进程。 | Apache-2.0 | 33,023 |
| [OpenTofu](../../entries/infra/opentofu.md) | 用声明式配置创建和变更云上资源，并作为 Terraform 改许可后的开源延续。 | MPL-2.0 | 30,440 |
| [Helm](../../entries/infra/helm.md) | 把一组 Kubernetes 资源配置打包成可版本化、可按环境改参数的图表。 | Apache-2.0 | 30,306 |
| [Cilium](../../entries/infra/cilium.md) | 用 eBPF 给 Kubernetes 提供网络、网络策略和流量可观测性。 | Apache-2.0 | 25,625 |

星标取自 GitHub API，统计日见各条目的 `stars_at`。星标只说明仓库被关注的程度，不代替采用率。PostgreSQL 这类镜像仓库星标偏低，仍然是行业默认选择。
