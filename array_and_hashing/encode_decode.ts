// Approach 1 — Length Prefix (Most Optimal)
function encode(strs: string[]): string {
  return strs.map((s) => `${s.length}#${s}`).join("");
}

function decode(s: string): string[] {
  const result: string[] = [];
  let i = 0;

  while (i < s.length) {
    let j = i;
    while (s[j] !== "#") j++;

    const length = parseInt(s.slice(i, j));
    const word = s.slice(j + 1, j + 1 + length);
    result.push(word);
    i = j + 1 + length;
  }

  return result;
}

// Approach 2 — Chunked Transfer Encoding
function encodeChunked(strs: string[]): string {
  let result = "";
  for (const s of strs) {
    const size = s.length.toString(16);
    result += size + "\r\n" + s + "\r\n";
  }
  result += "end\r\n\r\n";
  return result;
}

function decodeChunked(s: string): string[] {
  const result: string[] = [];
  let i = 0;

  while (i < s.length) {
    const j = s.indexOf("\r\n", i);
    const sizeStr = s.slice(i, j);

    if (sizeStr === "end") break;

    const size = parseInt(sizeStr, 16);
    const dataStart = j + 2;
    result.push(s.slice(dataStart, dataStart + size));
    i = dataStart + size + 2;
  }

  return result;
}
