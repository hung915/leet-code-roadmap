function groupAnagramsSort(strs: string[]): string[][] {
    const ans = new Map<string, string[]>();

    for (const str of strs) {
        const key = str.split('').sort().join('');
        if (!ans.has(key)) ans.set(key, []);
        ans.get(key)!.push(str);
    }

    return [...ans.values()];
}

function groupAnagramsAscii(strs: string[]): string[][] {
    const ans = new Map<string, string[]>();

    for (const str of strs) {
        const counter = new Array(26).fill(0);
        for (const char of str) counter[char.charCodeAt(0) - 97]++;
        const key = counter.join(',');
        if (!ans.has(key)) ans.set(key, []);
        ans.get(key)!.push(str);
    }

    return [...ans.values()];
}
