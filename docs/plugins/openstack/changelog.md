# Changelog

<!-- Changelogs are for humans, not machines. The end users of Rally project are
human beings who care about what's is changing, why and how it affects them.
Please leave these notes as much as possible human oriented. -->

<!-- Each release can use the next sections:
- **Added** for new features.
- **Changed** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features/plugins.
- **Removed** for now removed features/plugins.
- **Fixed** for any bug fixes. -->

<!-- Release notes for existing releases are MUTABLE! If there is something that
was missed or can be improved, feel free to change it! -->

## [1.1.0] - 2018-05-11

### Added

- [scenario plugin] GnocchiMetric.list_metric
- [scenario plugin] GnocchiMetric.create_metric
- [scenario plugin] GnocchiMetric.create_delete_metric
- [scenario plugin] GnocchiResource.create_resource
- [scenario plugin] GnocchiResource.create_delete_resource
- Introduce *__version__*, *__version_tuple__* at *rally_openstack* module.
  As like other python packages each release of *rally-openstack* package can
  introduce new things, deprecate or even remove other ones. To simplify
  integration with other plugins which depends on *rally-openstack*, the new
  properties can be used with proper checks.

### Changed

- [Docker image](https://hub.docker.com/r/xrally/xrally-openstack) ported
  to publish images from [rally-openstack](https://github.com/openstack/rally-openstack) repo instead of using the
  rally framework repository.
  Also, the CI is extended to check ability to build Docker image for any of
  changes.
- An interface of ResourceType plugins is changed since Rally 0.12. All our
  plugins are adopted to support it.
  The port is done in a backward compatible way, so the minimum required
  version of Rally still is 0.11.0, but we suggest you to use the latest
  release of Rally.

### Removed

- Calculation of the duration for "nova.bind_actions" action. It shows
  only duration of initialization Rally inner class and can be easily
  misunderstood as some kind of "Nova operation".
  Affects 1 inner scenario "NovaServers.boot_and_bounce_server".

### Fixed

- `required_services` validator should not check services which are
  configured via `api_versions@openstack` context since the proper validation
  is done at the context itself.
  The inner check for `api_versions@openstack` in `required_services`
  checked only `api_versions@openstack`, but `api_versions` string is also
  valid name for the context (if there is no other `api_versions` contexts
  for other platforms, but the case of name conflict is covered by another
  check).
- The endpoint_type defined in environment specification/deployment
  configuration is the endpoint interface for gnocchi.

## [1.0.0] - 2018-03-28

Start a fork of [rally/plugins/openstack module of original OpenStack Rally
project](https://github.com/openstack/rally/tree/0.11.1/rally/plugins/openstack)

### Added

- [scenario plugin] GnocchiArchivePolicy.list_archive_policy
- [scenario plugin] GnocchiArchivePolicy.create_archive_policy
- [scenario plugin] GnocchiArchivePolicy.create_delete_archive_policy
- [scenario plugin] GnocchiResourceType.list_resource_type
- [scenario plugin] GnocchiResourceType.create_resource_type
- [scenario plugin] GnocchiResourceType.create_delete_resource_type
- [scenario plugin] NeutronSubnets.delete_subnets
- [ci] New Zuul V3 native jobs
- Extend <existing@openstack> platform to support creating a specification based
  on system environment variables. This feature should be available with
  Rally>0.11.1

### Changed

- Methods for association and dissociation floating ips  were deprecated in
  novaclient a year ago and latest major release (python-novaclient 10)
  [doesn't include them](https://github.com/openstack/python-novaclient/blob/10.0.0/releasenotes/notes/remove-virt-interfaces-add-rm-fixed-floating-398c905d9c91cca8.yaml).
  These actions should be performed via neutronclient now. It is not as simple
  as it was via Nova-API and you can find more neutron-related atomic actions
  in results of scenarios.

### Removed

- *os-hosts* CLIs and python API bindings had been deprecated in
  python-novaclient 9.0.0 and became removed in [10.0.0 release](https://github.com/openstack/python-novaclient/blob/10.0.0/releasenotes/notes/remove-hosts-d08855550c40b9c6.yaml).
  This decision affected 2 scenarios [NovaHosts.list_hosts](https://rally.readthedocs.io/en/0.11.1/plugins/plugin_reference.html#novahosts-list-hosts-scenario)
  and [NovaHosts.list_and_get_hosts](https://rally.readthedocs.io/en/0.11.1/plugins/plugin_reference.html#novahosts-list-and-get-hosts-scenario)
  which become redundant and we cannot leave them (python-novaclient doesn't
  have proper interfaces any more).

### Fixed

- The support of [kubernetes python client](https://pypi.python.org/pypi/kubernetes) (which is used by Magnum plugins)
  is not limited by 3.0.0 max version. You can use more modern releases of that
  library.