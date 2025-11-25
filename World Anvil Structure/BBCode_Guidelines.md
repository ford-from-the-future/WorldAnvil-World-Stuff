# BBCode Guidelines for World Anvil

## What are BBCode tags?

A BBCode tag is a set of characters between square brackets. For example, `[b]` is a BBCode tag.

The characters inside the brackets determine the effect of the tag; in this case, `b` stands for bold, so it will apply bold formatting to the text between the tags. In edit mode, tags are always visible; in view mode, the tags disappear and their formatting is applied instead.

Many BBCode tags require an opening and a closing tag to tell the system when the tag's effect should end. Closing tags look like regular opening tags, but with a forward slash `/` in the beginning. For example, `[b]` is the opening tag, while `[/b]` is the closing tag.

---

## BBCode tags with options (aka. arguments)

In addition to single BBCode tags (like `[br]` for a line break), and those which need a closing tag (like `[b][/b]`), there are also tags with options! These options (technically known as "arguments") modify the behavior of the tag, giving you more advanced choices for formatting. Arguments are placed in the opening tag, and are separated by a colon `:` or a pipe `|`.

For example, the BBCode to embed an image looks like this `[img:5068227]`. Technically this has one "argument": the number that defines the image you want to use.

To center the image on your page, you can add an "argument" like this `[img:5068227|center]`. This tag has two arguments: the Image ID number (5068227) and the center alignment instruction.

Examples of other tags that use options are colored text, tooltips, and external links.

---

## List of tags

### Basic text formatting

| Tag | Example | Result |
|-----|---------|--------|
| `[b]...[/b]` | `[b]Bold text[/b]` | **Bold text** |
| `[i]...[/i]` | `[i]Italic text[/i]` | *Italic text* |
| `[u]...[/u]` | `[u]Underlined text[/u]` | <u>Underlined text</u> |
| `[s]...[/s]` | `[s]Strikethrough text[/s]` | ~~Strikethrough text~~ |
| `[small]...[/small]` | `[small]Smaller text[/small]` | Smaller text |
| `[sup]...[/sup]` | `This is [sup]superscript[/sup]` | This is <sup>superscript</sup> |
| `[sub]...[/sub]` | `This is [sub]subscript[/sub]` | This is <sub>subscript</sub> |
| `[dc]...[/dc]` | `[dc]T[/dc]his is a fancy drop cap...` | Fancy drop cap at start of paragraph |
| `[redacted:n]` | `This [redacted:4] is redacted` | This ████ is redacted |
| `[color:color\|background]...[/color]` | `[color:red\|yellow]This is red with yellow background.[/color]` | Colored text with background |
| `[noparse]...[/noparse]` | `[noparse]Use this to display [b]BBCode tags[/b][/noparse]` | Displays BBCode without formatting |
| `/* ... */` | `/* This will be hidden from view */` | Hidden comment (nothing shows) |
| `[mark]...[/mark]` | `[mark]This is highlighted![/mark]` | Highlighted text *(Grandmaster+)* |

### Headers

| Tag | Example |
|-----|---------|
| `[h1]...[/h1]` | `[h1]Level 1 header[/h1]` |
| `[h2]...[/h2]` | `[h2]Level 2 header[/h2]` |
| `[h3]...[/h3]` | `[h3]Level 3 header[/h3]` |
| `[h4]...[/h4]` | `[h4]Level 4 header[/h4]` |

### Layout containers

| Tag | Purpose | Example |
|-----|---------|---------|
| `[quote]...\|Author[/quote]` | Quote panel | `[quote]This is a quote.\|Author Name[/quote]` |
| `[aloud]...[/aloud]` | Highlight paragraph for reading aloud | `[aloud]Dialogue for RPG session[/aloud]` |
| `[code]...[/code]` | Monospaced font like code editor | `[code]print("hello")[/code]` |
| `[spoiler]...\|Label[/spoiler]` | Hidden content with reveal button | `[spoiler]Secret content.\|Click me![/spoiler]` |
| `[tooltip:tooltip text]...[/tooltip]` | Hover tooltip | `[tooltip:Hover text]Mouse over me[/tooltip]` |
| `--Label::Content--` | Custom sidebar field | `--Example::This mimics sidebar fields--` |

### Links

| Tag | Purpose | Example |
|-----|---------|---------|
| `[url:https://...]...[/url]` | External link | `[url:https://worldanvil.com]Visit World Anvil[/url]` |
| `@[Title](template:id)` | Article link | `@[Article Title](template:article-id)` |
| `[articleblock:id]` | Article block embed | `[articleblock:article-id-here]` |
| `[world:id]` | World link | `[world:7c0fec4d-9436-4325-90f5-cdbfdd3932b6]` |

### Anchors (jump links)

| Tag | Purpose | Example |
|-----|---------|---------|
| `[h3\|anchor-name]...[/h3]` | Create anchor point | `[h3\|section-one]Section One[/h3]` |
| `[url:#anchor-name]...[/url]` | Jump to anchor | `[url:#section-one]Go to Section One[/url]` |

### World Anvil content links

| Tag | Purpose |
|-----|---------|
| `[category:id]Name[/category]` | Link to category |
| `[blocklink:id]` | Link to statblock |
| `[timeline:id]Name[/timeline]` | Link to timeline |
| `[history:id]Event name[/history]` | Link to historical entry |
| `[worldmeta:id\|section]` | Embed world meta section |

### Embedding World Anvil content

| Tag | Purpose |
|-----|---------|
| `[book:id]` | Embed book-style category |
| `[map:id]` | Embed interactive map |
| `[block:id]` | Embed RPG statblock |
| `[img:id]` | Embed image |
| `[img:id\|alignment]` | Embed image with alignment |
| `[secret:id]` | Embed secret *(Guild+)* |
| `[manuscript:id]` | Embed manuscript *(Master+)* |
| `[familytree:id]` | Embed family tree *(Master+)* |
| `[diplomacy:id]` | Embed diplomacy web *(Master+)* |

### Paragraph formatting

| Tag | Purpose | Example |
|-----|---------|---------|
| `[br]` | Line break | `First line[br]Second line` |
| `[hr]` | Horizontal ruler | `Text above[hr]Text below` |
| `[in]...[/in]` | Indent paragraph | `[in]Indented text[/in]` |
| `[p]...[/p]` | Paragraph (usually use blank lines instead) | `[p]Paragraph text[/p]` |
| `[center]...[/center]` | Center text | `[center]Centered text[/center]` |

### Lists

**Unordered list:**
```
[ul]
- Item one
- Item two
[/ul]
```

**Ordered list:** (with `[ol]` instead of `[ul]`)

See documentation for sub-lists options.

### Columns

```
[row]
[col]
Left column content
[/col]
[col]
Right column content
[/col]
[/row]
```

### Tables

```
[table]
[tr]
[th]Header 1[/th]
[th]Header 2[/th]
[/tr]
[tr]
[td]Data 1[/td]
[td]Data 2[/td]
[/tr]
[/table]
```

### Icons

| Tag | Purpose |
|-----|---------|
| `[pin:icon_name]` | Pin/location icons |
| `[genesysdice:type]` | Genesys dice icons |
| `[pf:action]` | Pathfinder action icons |
| `[section:icon_class]...[/section]` | Section with icon *(Grandmaster+)* |

### Interactive dice roller

```
[roll:3d10]
```

Supports dice rolls for most RPG systems.

### Tables of contents and navigation tools

| Tag | Purpose |
|-----|---------|
| `[articletoc]` | Auto-generates TOC from headers in article |
| `[toc]` | World category table of contents |
| `[breadcrumb]` | Navigation breadcrumb trail |
| `[tagged:#tag\|list]` | List articles with tag |
| `[taggedblocks:#tag\|list]` | List statblocks with tag |

### Follow buttons

| Tag | Example |
|-----|---------|
| `[follow:Username]` | `[follow:Username]` |
| `[follow:user-id]` | `[follow:7c0fec4d-9436-4325-90f5-cdbfdd3932b6]` |

### Embed external content

| Tag | Purpose | Availability |
|-----|---------|--------------|
| `[pdf:url]` | Embed interactive PDF | Guild+ |
| `[youtube:url]` | Embed YouTube video | All users |
| `[soundcloud:url]` | Embed SoundCloud | All users |
| `[sketchfab:url]` | Embed Sketchfab model | All users |
| `[spotify:url]` | Embed Spotify track | All users |
| `[discord:server-id]` | Embed Discord server widget | All users |

### Current world date

```
[currentdate:world-id]
```

Display and embed current world date.

### User links and information

| Tag | Purpose |
|-----|---------|
| `[user:Username]` | Link to user |
| `[usercard:Username]` | Embed user card |

### Creative Commons licenses

| Tag | License |
|-----|---------|
| `[licence:cc-by]` | Attribution 4.0 International |
| `[licence:cc-by-sa]` | Attribution ShareAlike |
| `[licence:cc-by-nc]` | Attribution-NonCommercial |
| `[licence:cc-by-nd]` | Attribution-NoDerivs |
| `[licence:cc-by-nc-sa]` | Attribution-NonCommercial-ShareAlike |
| `[licence:cc-by-nc-nd]` | Attribution-NonCommercial-NoDerivs |

### Visibility controls (Grandmaster+)

| Tag | Purpose | Example |
|-----|---------|---------|
| `[userstate:follower]...[/userstate]` | Show only to followers | Content visible to followers only |
| `[subcontainer:ID]...[/subcontainer]` | Show to subscriber group | Private subscriber content |
| `[container:class]...[/container]` | Apply custom CSS class | Custom styled container |

---

## Quick tips

- **Arguments are separated by `:` or `\|`** - Use colons or pipes to add options to tags
- **Always close tags** - If you open a tag, remember to close it (e.g., `[b]` → `[/b]`)
- **Nesting works** - You can combine tags: `[b][i]Bold and italic[/i][/b]`
- **Use blank lines for paragraphs** - Instead of `[p]` tags, just leave empty lines between paragraphs
- **Subscription tiers matter** - Some advanced tags require Guild, Master, or Grandmaster subscriptions

---

## Resources

For more detailed information about specific tags, visit the World Anvil documentation within the editor itself. Most complex tags have dedicated help pages available through the World Anvil interface.
