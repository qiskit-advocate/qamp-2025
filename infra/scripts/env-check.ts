#!/usr/bin/env tsx
import * as fs from "fs";
import * as path from "path";

const required = [
  "NEXT_PUBLIC_SUPABASE_URL",
  "SUPABASE_ANON_KEY",
  "SUPABASE_SERVICE_ROLE_KEY",
  // add more if you want them required:
  // "NEXT_PUBLIC_SUPABASE_ANON_KEY",
  // "ANTHROPIC_API_KEY",
];

const optional = [
  "NEXT_PUBLIC_SUPABASE_ANON_KEY",
  "ANTHROPIC_API_KEY",
  "SNAPTRADE_API_KEY",
  "MARKETDATA_API_KEY",
  "CF_ACCOUNT_ID",
  "CF_API_TOKEN",
  "NEXT_PUBLIC_APP_URL",
  "NODE_ENV",
];

const envPath = path.join(process.cwd(), ".env");
if (!fs.existsSync(envPath)) {
  console.error("❌ .env file not found in project root");
  console.log("  Create it with:  notepad .env");
  process.exit(1);
}

const content = fs.readFileSync(envPath, "utf8");
const map = new Map<string, string>();
for (const line of content.split(/\r?\n/)) {
  const m = line.match(/^([^#=\s]+)\s*=\s*(.*)$/);
  if (m) map.set(m[1].trim(), m[2].trim());
}

let ok = true;
console.log("🔍 Checking required environment variables:\n");
for (const k of required) {
  const v = map.get(k);
  if (!v || v === "..." || v.includes("xxx")) {
    ok = false;
    console.log(`❌ ${k} — missing or placeholder`);
  } else {
    console.log(`✅ ${k}`);
  }
}

console.log("\nℹ️ Optional variables:");
for (const k of optional) {
  const v = map.get(k);
  if (v) console.log(`✅ ${k}`);
  else console.log(`⚠️ ${k} — not set (optional)`);
}

if (!ok) {
  console.error("\n❌ Some required variables are missing. Edit .env and try again.");
  process.exit(1);
}
console.log("\n✅ Env check passed.");
