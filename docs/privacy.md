# Privacy policy

**Effective 21 October 2026.**

This policy covers **Trinity Workspace**, the Google OAuth application registered under
Google Cloud project `175408714951`. It explains exactly what Google account data the
application reads, where that data travels, how long it is kept, and how to revoke its
access.

!!! info "What this policy does *not* cover"

    Trinity Workspace is a **personal, single-operator integration** — it connects one
    person's own Google account to their own workstation. It is operated by **Huihuo Zheng**
    as an individual, and it is **not** a service offered to other people.

    This policy is not a statement by Argonne National Laboratory or the ALCF, and it does
    not describe the Trinity platform documented elsewhere on this site. It describes only
    the OAuth application named above.

## Who to contact

| | |
|---|---|
| Operator | Huihuo Zheng (individual) |
| Contact | <zhenghh04@gmail.com> |
| Application | Trinity Workspace |
| Google Cloud project | `175408714951` |

## What the application does

Trinity Workspace lets its operator drive **their own** Gmail mailbox and Google Drive
through a command-line AI assistant instead of a browser — searching mail, drafting and
sending replies, listing and reading Drive files, and creating or updating documents.

It is built on the open-source [`workspace-mcp`](https://pypi.org/project/workspace-mcp/)
server, which runs **on the operator's own computers**. There is no hosted backend, no
shared server, and no account system. Nobody else can sign in to it.

## What Google data it accesses

The application requests the scopes below. It accesses data **only in the Google account
that granted consent** — that is, the operator's own account.

### Gmail

| Scope | What it permits |
|---|---|
| `gmail.readonly` | Read messages, threads, labels and attachments metadata |
| `gmail.send` | Send mail as the signed-in account |
| `gmail.compose` | Create and modify drafts |
| `gmail.modify` | Change labels, mark read/unread, archive |
| `gmail.labels` | Create and manage labels |
| `gmail.settings.basic` | Read basic settings such as signatures and filters |

### Google Drive

| Scope | What it permits |
|---|---|
| `drive.readonly` | List and read files and their contents |
| `drive.file` | Create files, and modify files the application itself created |
| `drive` | Full access, including sharing permissions on existing files |

### Identity

`openid`, `userinfo.email` and `userinfo.profile` — used solely to label which Google
account a stored credential belongs to, so the right one is selected.

## How the data is used

Google user data is used for **one purpose only**: carrying out the operator's own
explicit, interactive requests — "find the message from X", "reply to this thread",
"summarise that spreadsheet".

It is **not** used for advertising, profiling, analytics, resale, or any purpose the
operator did not directly ask for in the moment.

## Where the data goes

This is the part worth reading closely.

1. **Google's APIs → the operator's computer.** Requests are made directly to Google over
   HTTPS from a process running on hardware the operator controls. No intermediate server
   of ours receives them.

2. **The operator's computer → an AI model provider.** Trinity Workspace is a tool for an
   AI assistant. When the operator asks the assistant to act on their mail or files, the
   content returned by Google — message bodies, file contents, metadata — **is included in
   the prompt sent to a third-party large-language-model provider** (currently Anthropic,
   and in some configurations an Argonne-operated model gateway) so the model can answer.

    This transfer happens only as part of fulfilling a request the operator made, and only
    for the data relevant to that request. Those providers are bound by their own API terms,
    under which submitted content is **not used to train their models**. Even so, the
    operator should treat anything they ask the assistant to read as having been shared with
    the model provider, and avoid pointing it at material that may not leave Google under
    its own obligations.

3. **Nowhere else.** The data is not transferred to any other party, and is never sold,
   rented, or shared for advertising.

## Storage and retention

| What | Where | Retention |
|---|---|---|
| OAuth refresh/access tokens | Local disk on the operator's machine, in a directory readable only by the operator (mode `0600`) | Until revoked or deleted |
| Message and file content | Held in process memory for the duration of a request | Not written to any database |
| Conversation transcripts | Local disk on the operator's machine | May contain excerpts of mail or file content; retained locally until deleted |

There is no cloud database, no backup service, and no analytics pipeline. Deleting the
local credential directory and the local transcripts removes everything the application
holds.

## Artificial intelligence and machine learning

Google user data obtained through these scopes is **never** used to develop, train,
fine-tune, or improve any generalised artificial-intelligence or machine-learning model.
It is passed to a model only for inference, in order to answer the operator's immediate
request, as described above.

## Limited Use disclosure

Trinity Workspace's use and transfer of information received from Google APIs to any other
app will adhere to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements.

## Security

- Credentials are stored with owner-only file permissions and are never committed to source
  control, logged, or transmitted anywhere except to Google's token endpoint.
- All communication with Google uses TLS.
- The OAuth consent flow uses PKCE, and redirect URIs are restricted to a fixed allow-list
  registered in the Google Cloud console.
- The application is unverified by Google and is limited to a small number of users by
  Google's own policy. It is not offered to the public.

## Revoking access

The operator can withdraw this application's access at any time, without contacting anyone:

1. Visit [myaccount.google.com/permissions](https://myaccount.google.com/permissions).
2. Select **Trinity Workspace**.
3. Choose **Remove access**.

Revocation is immediate and invalidates the stored tokens. Deleting the local credential
directory removes the copy held on disk.

## Children

This application is not directed at children and is not available to them. It serves a
single adult operator.

## Changes to this policy

Material changes will be published on this page with a new effective date. The page's full
revision history is public in the
[trinity_hub repository](https://github.com/zhenghh04/trinity_hub/commits/main/docs/privacy.md).

## Questions

Write to <zhenghh04@gmail.com>.
