function unpackGiftbox(giftBox, wish) {
  if(giftBox.length === 0 ) return false; 
  for(let i = 0 ; i < giftBox.length; i++){
    if( giftBox[i] === wish) return true ;
    if( Array.isArray(giftBox[i]) && unpackGiftbox(giftBox[i],wish))  return true ;
  }
  return false; 
}
