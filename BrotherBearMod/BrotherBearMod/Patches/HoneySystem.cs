using HarmonyLib;
using MegaCrit.Sts2.Core.Entities.Cards;
using MegaCrit.Sts2.Core.Models;

namespace BrotherBearMod.Patches;

/// <summary>
/// 蜂蜜资源系统 - 熊二的核心机制
/// 攻击牌打出时获得蜂蜜
/// </summary>
public static class HoneySystem
{
    public const int MaxHoney = 10;
    public static int CurrentHoney { get; private set; }

    public static void AddHoney(int amount)
    {
        CurrentHoney = Math.Min(CurrentHoney + amount, MaxHoney);
    }

    public static bool ConsumeHoney(int amount)
    {
        if (CurrentHoney < amount) return false;
        CurrentHoney -= amount;
        return true;
    }

    public static void ResetHoney()
    {
        CurrentHoney = 0;
    }
}

/// <summary>
/// 攻击牌打出后获得蜂蜜
/// </summary>
[HarmonyPatch(typeof(CardModel), nameof(CardModel.OnPlay))]
[HarmonyPostfix]
public static class HoneyOnAttackPatch
{
    static void Postfix(CardModel __instance)
    {
        if (__instance.Type == CardType.Attack)
        {
            HoneySystem.AddHoney(1);
        }
    }
}
