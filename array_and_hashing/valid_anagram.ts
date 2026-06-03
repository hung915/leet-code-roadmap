function isAnagramCounter(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const counter = new Map<string, number>();

    for (let i = 0; i < s.length; i++) {
        counter.set(s[i], (counter.get(s[i]) ?? 0) + 1);
        counter.set(t[i], (counter.get(t[i]) ?? 0) - 1);
    }

    return [...counter.values()].every(v => v === 0);
}

function isAnagramTwoCounter(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const sCounter = new Map<string, number>();
    const tCounter = new Map<string, number>();

    for (let i = 0; i < s.length; i++) {
        sCounter.set(s[i], (sCounter.get(s[i]) ?? 0) + 1);
        tCounter.set(t[i], (tCounter.get(t[i]) ?? 0) + 1);
    }

    for (const [k, v] of sCounter) {
        if (tCounter.get(k) !== v) return false;
    }
    return true;
}

function isAnagramAscii(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const counter = new Array(26).fill(0);

    for (const char of s) counter[char.charCodeAt(0) - 97]++;

    for (const char of t) {
        if (counter[char.charCodeAt(0) - 97] === 0) return false;
        counter[char.charCodeAt(0) - 97]--;
    }

    return true;
}
