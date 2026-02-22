# HiGHS RPM Spec

[![Copr build status](https://copr.fedorainfracloud.org/coprs/mgrabovs/HiGHS/package/highs/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/mgrabovs/HiGHS/package/highs/)

This repository contains the RPM spec file for packaging the [HiGHS solver](https://highs.dev/). The package is built automatically in Fedora Copr after each HiGHS upstream release.

- HiGHS homepage: https://highs.dev/
- Upstream: https://github.com/ERGO-Code/HiGHS
- Copr: https://copr.fedorainfracloud.org/coprs/mgrabovs/HiGHS/

## Install (Fedora/Copr)

Enable the Copr repo and install the packages:

```bash
sudo dnf copr enable mgrabovs/HiGHS
sudo dnf install highs
```

For development headers and CMake/pkg-config files:

```bash
sudo dnf install highs-devel
```

## What's In This Repo

- `highs.spec` is the authoritative spec used by Copr.
- Source tarballs are pulled from the official HiGHS GitHub releases based on the `Version` in the spec.

## Packaging

- Local build (mock):

    ```bash
    mock -r fedora-rawhide-x86_64 --rebuild highs*.src.rpm
    ```

- Local build (rpmbuild):

    ```bash
    spectool -g -R highs.spec
    rpmbuild -ba highs.spec
    ```
