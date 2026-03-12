import { useState, useCallback } from "react";

const MENU = {
  espresso: {
    ingredients: { water: 50, milk: 0, coffee: 18 },
    cost: 1.5,
    emoji: "☕",
    description: "Bold & intense",
  },
  latte: {
    ingredients: { water: 200, milk: 150, coffee: 24 },
    cost: 2.5,
    emoji: "🥛",
    description: "Smooth & creamy",
  },
  cappuccino: {
    ingredients: { water: 250, milk: 100, coffee: 24 },
    cost: 3.0,
    emoji: "☕",
    description: "Frothy & rich",
  },
} as const;

type CoffeeName = keyof typeof MENU;

interface Resources {
  water: number;
  milk: number;
  coffee: number;
  money: number;
}

type Step = "idle" | "inserting_coins" | "brewing" | "done";

interface Message {
  text: string;
  type: "success" | "error" | "info" | "warning";
}

const INITIAL_RESOURCES: Resources = {
  water: 300,
  milk: 200,
  coffee: 100,
  money: 0,
};

export default function CoffeeMachine() {
  const [resources, setResources] = useState<Resources>(INITIAL_RESOURCES);
  const [step, setStep] = useState<Step>("idle");
  const [selectedCoffee, setSelectedCoffee] = useState<CoffeeName | null>(null);
  const [coins, setCoins] = useState({ quarters: 0, dimes: 0, nickles: 0, pennies: 0 });
  const [messages, setMessages] = useState<Message[]>([]);
  const [isOn, setIsOn] = useState(true);
  const [showReport, setShowReport] = useState(false);
  const [brewing, setBrewing] = useState(false);
  const [lastCoffee, setLastCoffee] = useState<CoffeeName | null>(null);

  const addMessage = useCallback((text: string, type: Message["type"]) => {
    setMessages((prev) => [{ text, type }, ...prev].slice(0, 6));
  }, []);

  const totalInserted = parseFloat(
    (coins.quarters * 0.25 + coins.dimes * 0.1 + coins.nickles * 0.05 + coins.pennies * 0.01).toFixed(2)
  );

  const handleSelectCoffee = (name: CoffeeName) => {
    if (!isOn) return;
    const { water, milk, coffee } = MENU[name].ingredients;
    if (resources.water < water) { addMessage("Sorry, there is not enough water.", "error"); return; }
    if (resources.milk < milk) { addMessage("Sorry, there is not enough milk.", "error"); return; }
    if (resources.coffee < coffee) { addMessage("Sorry, there is not enough coffee.", "error"); return; }
    setSelectedCoffee(name);
    setCoins({ quarters: 0, dimes: 0, nickles: 0, pennies: 0 });
    setStep("inserting_coins");
    addMessage(`Selected ${name}. Please insert coins.`, "info");
  };

  const adjustCoin = (coin: keyof typeof coins, delta: number) => {
    setCoins((prev) => ({ ...prev, [coin]: Math.max(0, prev[coin] + delta) }));
  };

  const handleMakeCoffee = () => {
    if (!selectedCoffee) return;
    const cost = MENU[selectedCoffee].cost;
    if (totalInserted < cost) {
      addMessage(`Not enough money. Need $${cost.toFixed(2)}, got $${totalInserted.toFixed(2)}.`, "error");
      return;
    }
    const change = parseFloat((totalInserted - cost).toFixed(2));
    setBrewing(true);
    setStep("brewing");
    setTimeout(() => {
      setResources((prev) => ({
        water: prev.water - MENU[selectedCoffee!].ingredients.water,
        milk: prev.milk - MENU[selectedCoffee!].ingredients.milk,
        coffee: prev.coffee - MENU[selectedCoffee!].ingredients.coffee,
        money: parseFloat((prev.money + cost).toFixed(2)),
      }));
      setLastCoffee(selectedCoffee);
      if (change > 0) addMessage(`Here is $${change.toFixed(2)} in change.`, "info");
      addMessage(`Here is your ${selectedCoffee}! Enjoy! ${MENU[selectedCoffee!].emoji}`, "success");
      setBrewing(false);
      setStep("done");
    }, 1800);
  };

  const handleReset = () => {
    setStep("idle");
    setSelectedCoffee(null);
    setCoins({ quarters: 0, dimes: 0, nickles: 0, pennies: 0 });
    setLastCoffee(null);
  };

  const handleTogglePower = () => {
    if (isOn) { setIsOn(false); setStep("idle"); setSelectedCoffee(null); setMessages([]); setShowReport(false); }
    else { setIsOn(true); addMessage("Machine powered on. Ready to brew!", "info"); }
  };

  const resourcePercent = (value: number, max: number) => Math.min(100, Math.round((value / max) * 100));

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-950 via-stone-900 to-amber-900 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <div className="relative bg-gradient-to-b from-stone-800 to-stone-900 rounded-3xl shadow-2xl border border-stone-700 overflow-hidden">

          {/* Header */}
          <div className="bg-gradient-to-r from-amber-800 to-amber-700 px-6 py-3 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${isOn ? "bg-green-400 shadow-[0_0_8px_#4ade80]" : "bg-stone-500"}`} />
              <span className="text-amber-100 font-bold text-lg tracking-wider">CAFÉ-O-MATIC</span>
            </div>
            <div className="flex items-center gap-3">
              <button onClick={() => setShowReport(!showReport)} disabled={!isOn}
                className="text-xs text-amber-200 hover:text-white px-2 py-1 rounded border border-amber-600 hover:border-amber-400 transition-colors disabled:opacity-40 disabled:cursor-not-allowed">
                📊 Report
              </button>
              <button onClick={handleTogglePower}
                className={`text-xs px-3 py-1 rounded border transition-colors font-semibold ${isOn ? "bg-red-800 text-red-200 border-red-600 hover:bg-red-700" : "bg-green-800 text-green-200 border-green-600 hover:bg-green-700"}`}>
                {isOn ? "⏻ Off" : "⏻ On"}
              </button>
            </div>
          </div>

          {/* Report */}
          {showReport && isOn && (
            <div className="bg-stone-800 border-b border-stone-700 px-6 py-4">
              <h3 className="text-amber-400 font-semibold text-sm mb-3">MACHINE REPORT</h3>
              <div className="grid grid-cols-2 gap-x-8 gap-y-2 text-sm">
                {[
                  { label: "Water", value: `${resources.water} ml`, max: 300, current: resources.water, color: "bg-blue-500" },
                  { label: "Milk", value: `${resources.milk} ml`, max: 200, current: resources.milk, color: "bg-yellow-300" },
                  { label: "Coffee", value: `${resources.coffee} g`, max: 100, current: resources.coffee, color: "bg-amber-700" },
                  { label: "Money", value: `$${resources.money.toFixed(2)}`, max: null, current: null, color: "" },
                ].map(({ label, value, max, current, color }) => (
                  <div key={label}>
                    <div className="flex justify-between text-stone-300 mb-1">
                      <span>{label}</span>
                      <span className="text-amber-300 font-mono">{value}</span>
                    </div>
                    {max && current !== null && (
                      <div className="h-1.5 bg-stone-600 rounded-full overflow-hidden">
                        <div className={`h-full ${color} rounded-full transition-all`} style={{ width: `${resourcePercent(current, max)}%` }} />
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="px-6 pt-6 pb-2">
            {/* Screen */}
            <div className="bg-stone-950 rounded-xl border border-stone-600 p-4 mb-5 min-h-[100px] relative overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-br from-green-900/10 to-transparent pointer-events-none" />
              {!isOn ? (
                <div className="text-stone-500 text-center py-4"><div className="text-4xl mb-2">⏻</div><div className="text-sm">Machine is off</div></div>
              ) : brewing ? (
                <div className="text-center py-2">
                  <div className="text-3xl animate-bounce mb-2">☕</div>
                  <div className="text-amber-400 text-sm font-mono animate-pulse">Brewing your {selectedCoffee}...</div>
                  <div className="mt-3 flex justify-center gap-1">
                    {[0,1,2,3,4].map(i => <div key={i} className="w-1.5 h-1.5 bg-amber-500 rounded-full animate-bounce" style={{ animationDelay: `${i * 0.15}s` }} />)}
                  </div>
                </div>
              ) : step === "done" ? (
                <div className="text-center py-2">
                  <div className="text-4xl mb-2">{lastCoffee ? MENU[lastCoffee].emoji : "☕"}</div>
                  <div className="text-green-400 font-semibold">Enjoy your {lastCoffee}!</div>
                  <button onClick={handleReset} className="mt-3 text-xs text-amber-400 hover:text-amber-300 border border-amber-700 hover:border-amber-500 px-3 py-1 rounded transition-colors">Order another</button>
                </div>
              ) : step === "inserting_coins" && selectedCoffee ? (
                <div>
                  <div className="text-amber-300 text-sm font-semibold mb-1">{selectedCoffee.charAt(0).toUpperCase() + selectedCoffee.slice(1)} — ${MENU[selectedCoffee].cost.toFixed(2)}</div>
                  <div className="text-stone-400 text-xs">Insert coins below, then press Make Coffee</div>
                  <div className="mt-2 flex items-center justify-between">
                    <span className="text-stone-400 text-xs">Inserted:</span>
                    <span className={`font-mono text-sm font-bold ${totalInserted >= MENU[selectedCoffee].cost ? "text-green-400" : "text-amber-300"}`}>
                      ${totalInserted.toFixed(2)} / ${MENU[selectedCoffee].cost.toFixed(2)}
                    </span>
                  </div>
                </div>
              ) : (
                <div className="text-center py-3">
                  <div className="text-amber-400 text-sm">Select a drink to get started</div>
                  <div className="text-stone-500 text-xs mt-1">Press any button below</div>
                </div>
              )}
            </div>

            {/* Coffee Buttons */}
            {step === "idle" && isOn && (
              <div className="grid grid-cols-3 gap-3 mb-5">
                {(Object.keys(MENU) as CoffeeName[]).map((name) => {
                  const item = MENU[name];
                  const canMake = resources.water >= item.ingredients.water && resources.milk >= item.ingredients.milk && resources.coffee >= item.ingredients.coffee;
                  return (
                    <button key={name} onClick={() => handleSelectCoffee(name)} disabled={!canMake}
                      className={`group flex flex-col items-center gap-1.5 py-4 px-2 rounded-xl border transition-all duration-200 ${canMake ? "bg-stone-700 border-stone-600 hover:bg-amber-900/50 hover:border-amber-600 hover:shadow-lg active:scale-95 cursor-pointer" : "bg-stone-800 border-stone-700 opacity-50 cursor-not-allowed"}`}>
                      <span className="text-2xl">{item.emoji}</span>
                      <span className="text-amber-200 text-sm font-semibold capitalize">{name}</span>
                      <span className="text-amber-500 text-xs font-mono">${item.cost.toFixed(2)}</span>
                      <span className="text-stone-400 text-xs">{item.description}</span>
                    </button>
                  );
                })}
              </div>
            )}

            {/* Coin Insertion */}
            {step === "inserting_coins" && selectedCoffee && (
              <div className="mb-5">
                <div className="text-stone-400 text-xs font-semibold mb-2 tracking-wider uppercase">Insert Coins</div>
                <div className="grid grid-cols-2 gap-2 mb-3">
                  {([
                    { key: "quarters", label: "Quarter", value: "25¢" },
                    { key: "dimes", label: "Dime", value: "10¢" },
                    { key: "nickles", label: "Nickel", value: "5¢" },
                    { key: "pennies", label: "Penny", value: "1¢" },
                  ] as const).map(({ key, label, value }) => (
                    <div key={key} className="bg-stone-800 rounded-lg border border-stone-600 p-3 flex items-center justify-between">
                      <div>
                        <div className="text-stone-300 text-xs font-semibold">{label}</div>
                        <div className="text-amber-500 text-xs">{value}</div>
                      </div>
                      <div className="flex items-center gap-2">
                        <button onClick={() => adjustCoin(key, -1)} className="w-7 h-7 rounded-lg bg-stone-700 text-stone-300 hover:bg-stone-600 hover:text-white flex items-center justify-center text-sm transition-colors active:scale-90">−</button>
                        <span className="text-amber-200 font-mono text-sm w-5 text-center">{coins[key]}</span>
                        <button onClick={() => adjustCoin(key, 1)} className="w-7 h-7 rounded-lg bg-amber-700 text-amber-100 hover:bg-amber-600 flex items-center justify-center text-sm transition-colors active:scale-90">+</button>
                      </div>
                    </div>
                  ))}
                </div>
                <div className="flex gap-2">
                  <button onClick={handleReset} className="flex-1 py-2.5 rounded-xl border border-stone-600 text-stone-400 hover:text-stone-200 hover:border-stone-400 text-sm transition-colors">Cancel</button>
                  <button onClick={handleMakeCoffee} disabled={totalInserted < (MENU[selectedCoffee]?.cost ?? 0)}
                    className={`flex-grow py-2.5 px-5 rounded-xl text-sm font-semibold transition-all ${totalInserted >= MENU[selectedCoffee].cost ? "bg-amber-700 hover:bg-amber-600 text-amber-100 shadow-lg active:scale-95" : "bg-stone-700 text-stone-500 cursor-not-allowed"}`}>
                    ☕ Make Coffee
                  </button>
                </div>
              </div>
            )}
          </div>

          {/* Message Log */}
          {messages.length > 0 && isOn && (
            <div className="mx-6 mb-5">
              <div className="bg-stone-950/80 rounded-xl border border-stone-700 p-3 space-y-1.5 max-h-32 overflow-y-auto">
                {messages.map((msg, i) => (
                  <div key={i} className={`text-xs flex items-start gap-1.5 ${msg.type === "success" ? "text-green-400" : msg.type === "error" ? "text-red-400" : msg.type === "warning" ? "text-yellow-400" : "text-stone-400"} ${i === 0 ? "opacity-100" : "opacity-60"}`}>
                    <span className="mt-0.5">{msg.type === "success" ? "✓" : msg.type === "error" ? "✕" : msg.type === "warning" ? "⚠" : "›"}</span>
                    {msg.text}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Resource Bar */}
          <div className="bg-stone-950/50 border-t border-stone-700 px-6 py-3 flex items-center justify-between">
            {[
              { label: "Water", value: resources.water, unit: "ml", max: 300, color: "bg-blue-500" },
              { label: "Milk", value: resources.milk, unit: "ml", max: 200, color: "bg-yellow-300" },
              { label: "Coffee", value: resources.coffee, unit: "g", max: 100, color: "bg-amber-700" },
            ].map(({ label, value, unit, max, color }) => (
              <div key={label} className="flex flex-col items-center gap-1 w-16">
                <div className="text-stone-500 text-xs">{label}</div>
                <div className="w-full h-1.5 bg-stone-700 rounded-full overflow-hidden">
                  <div className={`h-full ${color} rounded-full transition-all duration-700`} style={{ width: `${resourcePercent(value, max)}%` }} />
                </div>
                <div className="text-stone-400 text-xs font-mono">{value}{unit}</div>
              </div>
            ))}
            <div className="flex flex-col items-center gap-1">
              <div className="text-stone-500 text-xs">Revenue</div>
              <div className="text-amber-400 font-mono text-sm font-bold">${resources.money.toFixed(2)}</div>
            </div>
          </div>
        </div>
        <p className="text-center text-stone-600 text-xs mt-4">Interactive Coffee Machine Simulator</p>
      </div>
    </div>
  );
}