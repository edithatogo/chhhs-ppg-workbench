# Operating context and evidence boundary

## Supplied evidence from another session — 12 October 2026
The user reported successful QH SharePoint publication-register reads/updates,
reporting-folder CSV writes, and cloud-flow creation, solution association, runs
and readbacks in an existing RIMS environment. Some Clinical resource reads and
bounded writes were also reported. These are reusable execution patterns, not
proof of PPG-specific resources or a PPG deployment.

The publication registry (1,345 keyed publications plus 303 placeholders) is NOT
the PPG registry. The supplied PPG snapshot contained 985 entries. Never use the
publication totals, folders, solution or schedules as implicit PPG targets.

PAC/MCP authentication had expired (`AADSTS70043`): this does not prove permission
denial. Graph MCP had zero configured accounts. Mailbox read/send, Planner and
AI runtime/credits were not verified for the PPG project. Tool visibility is not
permission. Do not declare the whole environment unavailable based on one error.

A Clinical implementation session owned the shared browser at the time. That
historical observation is superseded for independent Neo work by the dated
coordination guidance below. Passwords/MFA are user-entered.

## Per-operation record, only when needed
Operation -> exact resource -> account/client -> authentication -> permissions or
licence -> actual result and timestamp. Distinguish reported evidence, local test,
synthetic run, tenant run and readback. Record expired auth, denied access,
unsupported operation, missing connection and unavailable licence separately.
Use `templates/operation-receipt.json` locally. Do not introduce tenant-wide tests
or app registration merely to configure an existing permitted pilot.

## Source location and local binding
The user supplied the master workbook URL and an XLSB copy. The exact tenant URL
is included only in the separate local-binding handover, not the Git tree. Copy
that file to `.local/deployment.json` in the approved environment. Do not invent
the still-unbound destination site, list IDs, solution or connections. Known source
path is recovered from the supplied binding, not by searching unrelated tenant data.

## Portfolio caution
The historical analysis proposed 33 directly associated CMO/EDMS entries and a much
larger CMO authorisation portfolio. These overlap in meaning and are provisional
role mappings, not verified current delegations. Never turn 434 authorising-officer
rows into 434 documents for the CMO to maintain. Resolve actual owners on the
selected family, not every record as a prerequisite.


## Cross-repository capability review — 15 October 2026

Inspected the six recent Clinical Hub/RIMS chats and their current AGENTS.md files,
plus RIMS authentication recovery and publication-platform acceptance records.
Thread reports are routing evidence; their saved native results were not independently
replayed in PPG. This review changes preparation guidance, not track completion.

### Local installation and tool exposure

The shared user plugin inventory contains ten Power Platform plugins, eleven
Power CAT plugins and Dataverse: 22 relevant entries installed and enabled.
Power Automate is 3.2.1, Dataverse 1.11.3 and Process Intelligence 0.7.0.
Use existing shared skills for a selected task; no duplicate per-repository MCP
registration or global installation is required. A plugin may supply skills
without exposing a connected tenant tool. Process Intelligence is optional;
its other-repository startup record is not PPG connection or data-use approval.
Its documented launcher uses Node 22; this shell's default Node is 26.11.1.

The current chat exposes M365 CLI MCP, BrowserOS Neo, FlowAgent, Power Platform,
Microsoft Learn and shell routes. M365 shell and MCP version calls both returned
12.0.0-beta.f682e10. PAC's banner reports 2.13.1, but `--version` was rejected
and a subsequent help call timed out after 10 seconds; PAC operation access
remains unqualified. Azure CLI reports 2.91.0.
M365 shell authentication status timed out after 20 seconds: authentication and
PPG target permission remain unqualified. No login/profile change was attempted.
Tool exposure and account metadata do not establish exact-target permissions.
The chat API exposes history/status, not the complete live tool catalogue,
sandbox configuration or effective tenant privileges of another chat. Recent
RIMS history records BrowserOS Neo and FlowAgent use; several sibling turns
ended with service 429 retry-limit failures, which are not tenant denials.

### Routing and coordination adopted for PPG

Use microsoft-cli-operations to select a bounded supported operation and
microsoft-365-auth for client-specific expiry recovery. SharePoint records/files
use the existing M365 CLI route; flow work uses qualified Power Automate/FlowAgent
routes, and solution packaging uses PAC only if the selected task needs it.
Retain a proved write route until preservation and saved readback parity establish
its replacement. Keep credentials inside the owning client. Classify PATH,
transport, authentication, permission, licence and application failures separately.
Do not infer tenant denial from expiry, timeout, service 429 or empty MCP accounts.

Independent BrowserOS Neo sessions/tabs may operate on disjoint authorised targets
without a global browser lease. Preserve other chats' forms and operation handles;
coordinate actual conflicts on the same tenant object/file, native window or shared
authentication-profile mutation. Sessions do not imply isolated credentials or
records. Verify the intended account and exact PPG target before tenant effects.
Other chats' approvals, recipient scope and tenant bindings are not PPG authority.

### Relevant delivery lessons

For QW1/QW3, retain the accounted raw snapshot and original source timestamps.
Keep importer fields separate from team edits, including legitimate zero/false
values. Use stable source-qualified identity rather than titles or row order.
For a multi-page import, freeze the source generation, account for every page,
read back stored contents, and advance the success checkpoint only after all
required writes reconcile. Existing files/records may be reused only when their
identity and intended contents match; material drift stops the affected write.

RIMS records that large embedded payload bodies made the native flow designer
unresponsive. Prefer bounded pages fetched from retained source data if QW3 needs
that scale. A connector can normalise timestamp text or reject bracketed property
names: preserve original source bytes, use explicit supported projections and
repair the observed mismatch. Do not assume these RIMS behaviours are already
proven for XLSB or implement an archive engine before it is needed.

After a real failure, preserve the operation handle and reconcile uncertain effects
before one cause-specific retry. Verify unchanged replay creates no duplicates and
preserves local edits; restore any temporary flow definition/state. Keep a short
handoff with exact next action, evidence level, blocker and changed retry condition.
Resume the retained operation after compaction rather than repeating discovery.

### Evidence sources inspected

- Clinical Hub: AGENTS.md, especially Microsoft skill collections, BrowserOS Neo
  freedom and expanded CLI routing (14 October 2026).
- RIMS: AGENTS.md, docs/AUTHENTICATION_RECOVERY.md and
  docs/PUBLICATION_PLATFORM_ACCEPTANCE.md, including the retained capture,
  commit-last archive, replay and stopped-state restoration records.
- Codex chat history: Clinical Hub native/support/platform lanes and RIMS
  archive/reconciliation/DOI lanes; observed 15 October 2026.
- Current-host plugin inventory and bounded local/MCP version checks.

Exact tenant bindings, source records and operational receipts remain outside Git.
QW2 remains independent of QW3; no additional track or runtime is introduced.

### Historical initial VS Code route qualification — 15 October 2026

Conductor checked the existing `spe` MCP registration and Azure CLI route rather
than starting a new login. SPE status sees the intended QH user/tenant, with no
owning app/container provisioned. A bounded Azure CLI GET of the known PPG source
web through its SharePoint resource audience returned `invalid_request` and an
interactive-authentication requirement. This is resource/client authentication,
not a confirmed permission denial. The standalone M365 status/device challenge
started by Conductor was cancelled; its prior code is no longer an active request.
The separate Microsoft 365 Graph MCP reports no valid token and zero accounts.

Use the already qualified authenticated Neo PPG source route for bounded reads
and intended destination inspection while supported CLI recovery remains pending.
Do not infer SPO permission from SPE/Azure status or copy VS Code/browser tokens
into another client. Do not create an embedded owning app as an ordinary List
access workaround. Preserve qualified routes and actual per-object ownership.

This dated client check is not a blocker for the subsequently qualified native
SharePoint/Excel flow connections. Follow the current [system delivery evidence](workbench-delivery.md)
and [handoff](../conductor/handoff.md); do not repeat authentication merely because
this earlier client observation remains in history.

## CLI-first route — 18 October 2026

User preference: use CLI wherever qualified. Live read-only checks confirmed the
existing intended-account connection works for Graph self licences, both PPG
SharePoint webs, Review Queue and evidence-library metadata. Private results are
in `.local/maturity-priority-20261018/`. The active saved name is retained in private
`connection-route.json`; inspect current `m365 connection list` and `m365 status`
before use, without printing credentials. Authentication is browser, app ID
`7ea7c24c-b1f6-4a20-9d11-9ae12e9e7ac0` (Microsoft 365 Agents Toolkit).
This supersedes earlier CLI-unavailable observations for these operations only.

Reuse the valid session. Do not reset shared authentication while another owner is
working. When renewal is genuinely necessary, preserve operations, coordinate the
shared connection change and use the same supported app/tenant/flow mapping.
If a supported device-code flow issues a fresh verification URL/code, use the
internal browser to open that exact URL and enter the code; do not routinely ask
the user to perform those mechanical steps. Browser-flow renewal should use its
actual authorization URL and supported callback. The current working flow is
browser, so do not force device code merely to match a remembered recipe.
Passwords, MFA and new consent remain user-controlled; stop at such an actual
challenge and describe it precisely. A prior unchanged Conditional Access denial
is not permission to cycle app IDs. Never copy VS Code/browser tokens or caches.

M365 supports `--appId`, `--tenant`, `--authType` and `--connectionName`; resolve the
tenant from private existing configuration. Do not transplant these flags into
PAC/Azure clients that lack that delegated mapping. Use existing Microsoft CLI/auth
skills and current installed help; no app registration or permission grant.
Distinguish wrong profile, expired auth, unsupported callback, transport failure,
403/Conditional Access, DLP and licensing. After renewal verify intended identity
and one exact-target read. Reuse successful evidence until drift or a new action
requires a check. Use native UI only for unsupported operations, actual artifact
inspection, ordinary-user proof or the authentication interaction itself.

For mutations follow existing same-client ETag/create-only/recovery protections;
GET success does not prove safe writes, no subscribers, ordinary-user access or
clinical authority. A blocked optional route must not stop independent saved-view,
manual recording or existing-report work.


### Existing-flow management fallback — 18 October 2026

A client-specific FlowAgent Azure sign-in failure occurred before submission; the
existing authenticated native run form remained usable. The current qualified
M365CLI connection subsequently passed stop, definition PATCH and start on one
explicitly unmanaged, solely owned fictional case-work flow. Each management
operation used an exact method/URL/body digest, one-send transport guard and no
redirects, with complete raw native definition/reference/state readback. Owner,
environment and installed references were preserved; no admin route, managed
override, authentication transfer, consent or permission change was used.

Reuse exact preimages and current-target checks before another operation. The
pre-save last-modified check is not an atomic server-side conditional save;
preserve one writer and reconcile an uncertain result before any retry. This
qualification is scoped to the observed existing flow and account, not tenant
administration or ordinary-user execution. Private native receipts are referenced
in current lifecycle metadata. The original SharePoint mutation guard is unchanged.

### Default-resource renewal — 22 October 2026

The installed CLI `status` command ensures its default Graph resource before
displaying identity. During source-preparation qualification it returned
AADSTS70043 (sign-in-frequency expiry), even though the same client's existing
SharePoint SDK token had just completed bounded uploads. Classify the affected
resource; do not infer a SharePoint permission or licensing denial from that banner.
The CLI reader remained held at its identity preflight rather than bypassing it.

The existing browser client was renewed for its exact default Graph resource
through the qualified SDK `form_post` route and normal `Auth.ensureAccessToken`
persistence. The human completed password/MFA. Intended account/app/tenant status,
actual SharePoint lookup and unchanged publisher replay subsequently passed. No
new client, scopes, consent, permissions or token/cache transfer was introduced.
Native desktop UI was unavailable; the in-app Browser completed the same-client
authorization flow. Private intent/result and callback evidence remain with the
source-preparation qualification; do not reuse an old authorization URL or restart
an already-live renewal process.

### Interactive renewal diagnostic — 18 October 2026

A renewal banner is not exact-resource access proof. The installed M365 client
can renew its default resource while the required SharePoint or flow-resource
session remains unavailable. Keep one existing renewal owner and verify the
intended account/tenant plus one bounded target read before resuming writes.

Microsoft's [MSAL AuthenticationResult contract](https://learn.microsoft.com/en-us/javascript/api/%40azure/msal-node/authenticationresult?view=msal-js-latest)
allows `account` to be null. A nullable-account dereference in a private renewal
script is therefore a diagnostic failure, not a successful login or a classified
Conditional Access denial. Preserve the result as unqualified. SDK-provided ID
claims may supply the exact expected principal and tenant when present; absent
or mismatched identity must still refuse. Do not manufacture account metadata,
transfer tokens between clients, print bearer material or relax the identity gate.
If further diagnosis is needed, retain only presence/type booleans for account,
ID claims, tenant and access-token fields; a fresh target read is still required.

The current native owner retains the failed attempt and determines the supported
changed route. Repeated unchanged sign-in attempts do not resolve the failure.
Password/MFA/consent remains user-controlled; no app, scope, permission or licence
change follows from this diagnostic. Local source tests and prepared flow pairs
can continue independently, but they do not qualify native execution.

`tools/lifecycle/validate_renewal_identity.mjs` is a tested pure helper for this
specific failure. The existing renewal owner may call
`validateRenewalIdentity(result, {username, tenantId, appId, objectId})` before
returning the existing SDK result to the client's normal persistence path.
The configured client's name/app/tenant checks remain in the existing script;
this helper does not establish which client made the request. `objectId` can
pin an already known native principal. Missing or conflicting identity refuses.
An absent/incomplete account requires SDK-provided principal, tenant and client
ID claims; the helper does not decode bearer tokens or invent an account.
Its result explicitly leaves target access and native writes unqualified. Keep
the bounded native read afterward. The helper performs no sign-in, imports no
SDK and does not access or change credentials, caches or native configuration.

The later owned renewal isolated an initialization error in the private direct-
SDK shim: the installed CLI request singleton had no logger. Its network client
caught the pre-transport exception and substituted an empty HTTP 400 response,
which produced an unusable authentication result. An offline reproduction made
no network request. Initializing `request.logger` with the same quiet logger
before using the SDK corrected this path; no installed SDK files were changed.
The existing form-post renewal then returned a nonempty token and exact expected
account/tenant, persisted normally, and passed independent CLI identity plus
owned Flow and SharePoint target reads. This supersedes the empty-result blocker
for that session only. Keep debug output disabled and never treat a missing token
as success, even when some SDK identity fields exist.

## Recover the working tool route before declaring a blocker — 22 October 2026

User-directed reconciliation checked this chat's private receipts and the active
Clinical Hub native-flow and RIMS integration chats/repository guidance. The
working routes were retained; asking the user to rediscover the tool or supply a
URL is not the first step. Distinguish a functioning discovery tool from a missing
suitable deployment destination.

| Operation | Existing route | Actual scope and limits |
| --- | --- | --- |
| SharePoint/Graph and scoped Flow API | Saved Microsoft 365 Agents Toolkit client described above; normal same-client SDK persistence | Quiet request logger must be initialized before direct SDK use. Qualified ARM Flow endpoint uses management resource; Draft saves and Published readback are distinct. No cache/token transfer or unchanged denied-audience retry. |
| Dataverse discovery | `pac env list` | Global Discovery Service lists Dataverse organizations; it is not proof of all tenant environments. |
| User-accessible environment discovery | `pac environment-management list-environments-for-user --top 100`, or matching Power Platform MCP tool | Fresh MCP call succeeded with the existing intended PAC account and returned Default and Developer. This independently corroborates the earlier GDS result; not tenant-wide absence proof. Inspect pagination/response if the result reaches the requested limit. |
| Solutions and component queries | Existing PAC, explicit `--environment` URL for solution/FetchXML operations | Do not change the shared selected profile. An environment URL is not accepted by every preview command; inspect that exact command's help. |
| Native rendering, publication and unsupported API steps | Existing independent BrowserOS Neo tab, preserving object ownership | Use actual saved/run/file readback. Native Publish can activate a manual-flow copy; bounded restore used immediate Stop and verified zero runs. |
| FlowAgent | Only after inspecting its configured provider/account and exact operation | Its separate Azure/MSAL provider is not automatically the saved Toolkit or VS Code identity. Do not restart login or assume its failure invalidates another qualified route. |

Installed PAC at both the .dotnet-tools and VS Code-extension paths reports
2.13.1. The working help syntax is `pac <group> help` or
`pac <group> <command> help`; the tested `--help` and leading `pac help ...`
forms were rejected. Clinical Hub independently uses the .dotnet-tools path,
explicit environment IDs for preview flow reads, and Neo for native actions.
RIMS documents separate Fabric credentials and the same operation-specific
PAC/M365/browser fallback principle; Fabric access supplies no Dataverse rights.

Current discovery is successful, not an authentication/tool-access blocker.
Default holds the maintained unmanaged PPG workload; Developer holds the originating
unmanaged Word pilot. Managed testing still needs a suitable downstream target;
no existing workload may be deleted/converted merely to reuse its environment.
No new environment, connection, consent, role, licence or pipeline was created.
The user need only supply a target if one exists outside the accessible results;
repeat discovery only for changed evidence or a concrete additional route.

Private fresh tool response: `.local/ppg-alm/route-reconciliation-20261022/`.


### User-authorised isolated target creation supersedes discovery-only hold

On 22 October the user authorised creating an isolated test environment using
existing rights/licensing. One `pac admin create --type Developer --region
australia --currency AUD --language 1033 --async` operation succeeded; the exact
name/domain/operation ID and URL are private. `pac admin status` tracked that
original operation; GDS and exact target reads confirmed the new environment even
while the first user-environment list still lagged. Do not repeat creation on a
listing delay. Managed configuration import/upgrade/recovery now passes in that
Developer Basic target; two references remain unbound, with zero runs and final
Stopped. No source profile selection, paid enablement or consent was needed.
See the [bounded deployment runbook](repository-alm-plan-20261018.md#isolated-managed-configuration-deployment-qualified--22-october-2026).

PAC FetchXML via this .dotnet-tools invocation rejected embedded double-quote
attributes with an unexpected backslash XML error. Valid single-quoted XML
attributes succeeded without changing the query semantics/auth or native data.
Retain failed output and use distinct readback files. Native Flow service expands
reference declarations into connector presentation; verify explicit logical/API/
invoker mappings rather than treating that representation difference as a failed
import or silently rewriting the Dataverse declaration.


### Target connections, native fallback and version reads — 22 October 2026

The actual target OAuth status and bindings now pass. Native BrowserOS app UI
through computer use completed the owned Word dialog when Neo background-tab DOM
observations stayed blank/stale. Same target/account/browser session was retained;
this was not another auth client or a consent workaround. Existing OneDrive was
reconciled from PAC JSON, Word used one Create and the signed-in account. PAC
`connectivity list-connections --json` exposes status/account/target; its table
view alone does not. `pac connection create` is a service-principal Dataverse
credential command, not this OAuth route; no such credential was created.

Reimport with `pac solution import --settings-file` bound the managed references
without activation. A separate bounded native activation/Run then succeeded and
was stopped through the already qualified ARM management endpoint. Full target
and source readback is retained. Do not retry an uncertain Create or Run.

Word ignored the generic library URL's view hint, auto-saving a later version
before explicit Viewing. Keep original bytes/receipt and later edit history
separate. The existing Toolkit SharePoint resource can read native history and
`GetFileById(...)/versions(<observed-ID>)/$value`; the direct `_vti_history` path
returned401 with that bearer route. The changed REST read succeeded without new
scope/login; never repeat the unchanged401 or silently promote later bytes into
the generation receipt. See the current managed target runbook for exact scope.
